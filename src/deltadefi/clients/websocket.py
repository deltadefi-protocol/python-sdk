import asyncio
from collections.abc import Callable
import json
import logging
from typing import Any

import websockets

from deltadefi.error import ClientError


class WebSocketClient:
    """
    WebSocket client for DeltaDeFi real-time data streams.

    Supports:
    - Recent trades
    - Account streams
    - Market price streams
    - Market depth streams
    """

    def __init__(
        self,
        base_url: str = "wss://stream-staging.deltadefi.io",
        api_key: str | None = None,
        auto_reconnect: bool = True,
        reconnect_interval: int = 5,
        ping_interval: int = 20,
        ping_timeout: int = 10,
    ):
        """
        Initialize the WebSocket client.

        Args:
            base_url: WebSocket base URL
            api_key: API key for authentication
            auto_reconnect: Whether to automatically reconnect on disconnect
            reconnect_interval: Seconds to wait before reconnection attempt
            ping_interval: Seconds between ping frames
            ping_timeout: Timeout for pong response
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.auto_reconnect = auto_reconnect
        self.reconnect_interval = reconnect_interval
        self.ping_interval = ping_interval
        self.ping_timeout = ping_timeout

        self.websocket: websockets.WebSocketClientProtocol | None = None
        self.subscriptions: dict[str, dict[str, Any]] = {}
        self.message_handlers: dict[str, Callable] = {}
        self.is_connected = False
        self.should_stop = False

        self.logger = logging.getLogger(__name__)

    async def connect(self, endpoint_path: str = "") -> None:
        """
        Establish WebSocket connection.

        Args:
            endpoint_path: Specific endpoint path for the connection
        """
        try:
            # Build the full WebSocket URL
            if endpoint_path:
                url = f"{self.base_url}{endpoint_path}"
            else:
                url = f"{self.base_url}/ws"

            # Add API key as query parameter if provided
            if self.api_key:
                separator = "&" if "?" in url else "?"
                url = f"{url}{separator}api_key={self.api_key}"

            self.websocket = await websockets.connect(
                url,
                ping_interval=self.ping_interval,
                ping_timeout=self.ping_timeout,
            )
            self.is_connected = True
            self.logger.info(f"WebSocket connected successfully to {url}")

            # Start message listening loop
            self._listen_task = asyncio.create_task(self._listen_messages())

        except Exception as e:
            self.logger.error(f"Failed to connect to WebSocket: {e}")
            raise ClientError(0, "WS_CONNECTION_ERROR", str(e), {}, None) from e

    async def disconnect(self) -> None:
        """Close WebSocket connection."""
        self.should_stop = True
        if self.websocket:
            await self.websocket.close()
            self.is_connected = False
            self.logger.info("WebSocket disconnected")

    async def _listen_messages(self) -> None:
        """Listen for incoming WebSocket messages."""
        if not self.websocket:
            return

        try:
            async for message in self.websocket:
                if self.should_stop:
                    break

                await self._handle_message(message)

        except websockets.exceptions.ConnectionClosed:
            self.is_connected = False
            self.logger.warning("WebSocket connection closed")

            if self.auto_reconnect and not self.should_stop:
                await self._reconnect()

        except Exception as e:
            self.logger.error(f"Error in message listener: {e}")

    async def _handle_message(self, message: str | bytes) -> None:
        """Handle incoming WebSocket message."""
        try:
            # Convert bytes to string if needed
            message_str = (
                message.decode("utf-8") if isinstance(message, bytes) else message
            )
            data = json.loads(message_str)

            # Determine message type based on structure
            if isinstance(data, list) and len(data) > 0 and "timestamp" in data[0]:
                # This is a trade stream message (array format)
                if "trade" in self.message_handlers:
                    await self.message_handlers["trade"](data)
                else:
                    self.logger.debug("No handler for trade stream")

            elif isinstance(data, dict) and "type" in data:
                # Handle typed messages (account, price, etc.)
                msg_type = data.get("type", "unknown").lower()
                sub_type = data.get("sub_type", "").lower()

                if msg_type == "account":
                    # Account stream message
                    if "account" in self.message_handlers:
                        await self.message_handlers["account"](data)
                    else:
                        self.logger.debug("No handler for account stream")

                elif msg_type == "market" and sub_type == "market_price":
                    # Price stream message
                    if "price" in self.message_handlers:
                        await self.message_handlers["price"](data)
                    else:
                        self.logger.debug("No handler for price stream")

                else:
                    self.logger.debug(
                        f"Unknown message type: {msg_type}, sub_type: {sub_type}"
                    )

            elif (
                isinstance(data, dict)
                and "timestamp" in data
                and ("bids" in data or "asks" in data)
            ):
                # This is a depth stream message
                if "depth" in self.message_handlers:
                    await self.message_handlers["depth"](data)
                else:
                    self.logger.debug("No handler for depth stream")

            else:
                self.logger.debug(f"Unknown message format: {data}")

        except json.JSONDecodeError:
            message_repr = (
                message.decode("utf-8") if isinstance(message, bytes) else message
            )
            self.logger.error(f"Failed to parse message: {message_repr}")
        except Exception as e:
            self.logger.error(f"Error handling message: {e}")

    async def _reconnect(self) -> None:
        """Attempt to reconnect WebSocket."""
        self.logger.info(
            f"Attempting to reconnect in {self.reconnect_interval} seconds"
        )
        await asyncio.sleep(self.reconnect_interval)

        try:
            # For now, just reconnect to the first subscription if any exist
            # In a more complex implementation, you'd want to handle multiple concurrent subscriptions
            if self.subscriptions:
                first_sub = next(iter(self.subscriptions.values()))
                # Always use the stored endpoint for reconnection
                await self.connect(first_sub["endpoint"])
            else:
                await self.connect()

        except Exception as e:
            self.logger.error(f"Reconnection failed: {e}")
            if self.auto_reconnect and not self.should_stop:
                await self._reconnect()

    async def _send_message(self, message: dict[str, Any]) -> None:
        """Send message to WebSocket server."""
        if not self.websocket or not self.is_connected:
            raise ClientError(
                0, "WS_NOT_CONNECTED", "WebSocket not connected", {}, None
            )

        try:
            await self.websocket.send(json.dumps(message))
        except Exception as e:
            self.logger.error(f"Failed to send message: {e}")
            raise ClientError(0, "WS_SEND_ERROR", str(e), {}, None) from e

    def register_handler(self, stream_type: str, handler: Callable) -> None:
        """
        Register a message handler for a specific stream type.

        Args:
            stream_type: Type of stream (e.g., 'trade', 'depth', 'price', 'account')
            handler: Async function to handle messages
        """
        self.message_handlers[stream_type] = handler

    async def subscribe_trades(self, symbol: str) -> None:
        """
        Subscribe to recent trades for a symbol using DeltaDeFi's specific endpoint.

        Args:
            symbol: Trading pair symbol (e.g., "ADAUSDM")
        """
        if not self.api_key:
            raise ClientError(
                0, "API_KEY_REQUIRED", "API key required for trade streams", {}, None
            )

        # Close existing connection if any
        if self.websocket:
            await self.disconnect()

        # Connect to the specific trades endpoint
        endpoint_path = f"/market/recent-trades/{symbol}?limit=50"
        await self.connect(endpoint_path)

        # Store subscription info
        self.subscriptions[f"trade_{symbol}"] = {
            "type": "trade",
            "symbol": symbol,
            "endpoint": endpoint_path,
        }
        self.logger.info(f"Subscribed to trades for {symbol}")

    async def subscribe_depth(self, symbol: str) -> None:
        """
        Subscribe to market depth for a symbol using DeltaDeFi's specific endpoint.

        Args:
            symbol: Trading pair symbol (e.g., "ADAUSDM")
        """
        if not self.api_key:
            raise ClientError(
                0, "API_KEY_REQUIRED", "API key required for depth streams", {}, None
            )

        # Close existing connection if any
        if self.websocket:
            await self.disconnect()

        # Connect to the specific depth endpoint
        endpoint_path = f"/market/depth/{symbol}"
        await self.connect(endpoint_path)

        # Store subscription info
        self.subscriptions[f"depth_{symbol}"] = {
            "type": "depth",
            "symbol": symbol,
            "endpoint": endpoint_path,
        }
        self.logger.info(f"Subscribed to depth for {symbol}")

    async def subscribe_price(self, symbol: str) -> None:
        """
        Subscribe to price streams for a symbol using DeltaDeFi's specific endpoint.

        Args:
            symbol: Trading pair symbol (e.g., "ADAUSDM")
        """
        if not self.api_key:
            raise ClientError(
                0, "API_KEY_REQUIRED", "API key required for price streams", {}, None
            )

        # Close existing connection if any
        if self.websocket:
            await self.disconnect()

        # Connect to the specific price endpoint
        endpoint_path = f"/market/market-price/{symbol}"
        await self.connect(endpoint_path)

        # Store subscription info
        self.subscriptions[f"price_{symbol}"] = {
            "type": "price",
            "symbol": symbol,
            "endpoint": endpoint_path,
        }
        self.logger.info(f"Subscribed to price for {symbol}")

    async def subscribe_account(self) -> None:
        """
        Subscribe to account streams using DeltaDeFi's specific endpoint.
        Provides balance updates and order status updates.
        """
        if not self.api_key:
            raise ClientError(
                0, "API_KEY_REQUIRED", "API key required for account streams", {}, None
            )

        # Close existing connection if any
        if self.websocket:
            await self.disconnect()

        # Connect to the account stream endpoint
        endpoint_path = "/accounts/stream"
        await self.connect(endpoint_path)

        # Store subscription info
        self.subscriptions["account"] = {"type": "account", "endpoint": endpoint_path}
        self.logger.info("Subscribed to account streams")

    async def unsubscribe(self, subscription_key: str) -> None:
        """
        Unsubscribe from a stream.

        Args:
            subscription_key: Key of the subscription to cancel
        """
        if subscription_key not in self.subscriptions:
            return

        sub_data = self.subscriptions[subscription_key]
        message = {
            "method": "UNSUBSCRIBE",
            "params": sub_data["params"],
            "id": sub_data["id"],
        }

        await self._send_message(message)
        del self.subscriptions[subscription_key]
        self.logger.info(f"Unsubscribed from {subscription_key}")

    async def unsubscribe_all(self) -> None:
        """Unsubscribe from all streams."""
        for sub_key in list(self.subscriptions.keys()):
            await self.unsubscribe(sub_key)
