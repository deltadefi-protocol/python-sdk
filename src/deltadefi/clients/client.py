from sidan_gin import Wallet, decrypt_with_cipher

from deltadefi.clients.accounts import Accounts
from deltadefi.clients.app import App
from deltadefi.clients.markets import Market
from deltadefi.clients.orders import Order
from deltadefi.clients.points import Points
from deltadefi.clients.websocket import WebSocketClient
from deltadefi.models.models import OrderSide, OrderType
from deltadefi.responses import (
    CancelAllOrdersResponse,
    CancelOrderResponse,
    PostOrderResponse,
)


class ApiClient:
    """
    ApiClient for interacting with the DeltaDeFi API.
    """

    def __init__(
        self,
        network: str = "preprod",
        api_key: str | None = None,
        base_url: str | None = None,
        ws_url: str | None = None,
        master_wallet: Wallet | None = None,
    ):
        """
        Initialize the ApiClient.

        Args:
            network: The network to connect to ("mainnet" or "preprod").
            api_key: The API key for authentication.
            base_url: Optional; The base URL for the API.
            ws_url: Optional; The WebSocket URL for streaming.
            master_wallet: Optional; An instance of Wallet for signing transactions.
        """
        if network == "mainnet":
            self.network_id = 1
            self.base_url = "https://api.deltadefi.io"
            self.ws_url = "wss://stream.deltadefi.io"
        else:
            self.network_id = 0
            self.base_url = "https://api-staging.deltadefi.io"
            self.ws_url = "wss://stream-staging.deltadefi.io"

        if base_url:
            self.base_url = base_url

        if ws_url:
            self.ws_url = ws_url

        self.api_key = api_key
        self.master_wallet = master_wallet

        self.accounts = Accounts(base_url=self.base_url, api_key=api_key)
        self.app = App(base_url=self.base_url, api_key=api_key)
        self.orders = Order(base_url=self.base_url, api_key=api_key)
        self.markets = Market(base_url=self.base_url, api_key=api_key)
        self.points = Points(base_url=self.base_url, api_key=api_key)
        self.websocket = WebSocketClient(base_url=self.ws_url, api_key=api_key)

    def load_operation_key(self, password: str):
        """
        Load the operation key from the wallet using the provided password.

        Args:
            password: The password to decrypt the operation key.

        Returns:
            The decrypted operation key.
        """
        res = self.accounts.get_operation_key()
        operation_key = decrypt_with_cipher(res["encrypted_operation_key"], password)
        self.operation_wallet = Wallet.new_root_key(operation_key)

    def post_order(
        self,
        symbol: str,
        side: OrderSide,
        type: OrderType,
        base_quantity: str | None = None,
        quote_quantity: str | None = None,
        **kwargs,
    ) -> PostOrderResponse:
        """
        Post an order to the DeltaDeFi API. It includes building the transaction,
        signing it with the wallet, and submitting it.

        Args:
            symbol: The trading pair symbol (e.g., "ADAUSDM").
            side: The side of the order ("buy" or "sell").
            type: The type of the order ("limit" or "market").
            base_quantity: The quantity in base asset (e.g., ADA). Mutually exclusive with quote_quantity.
            quote_quantity: The quantity in quote asset (e.g., USDM). Mutually exclusive with base_quantity.
            price: Required for limit orders; The price for the order.
            max_slippage_basis_point: Optional; The maximum slippage in basis points for market orders.
            post_only: Optional; If True, the order will only be placed if it would be a maker order.

        Returns:
            A PostOrderResponse object containing the response from the API.

        Raises:
            ValueError: If the wallet is not initialized or quantity params are invalid.
        """
        if not hasattr(self, "operation_wallet") or self.operation_wallet is None:
            raise ValueError("Operation wallet is not initialized")

        build_res = self.orders.build_place_order_transaction(
            symbol,
            side,
            type,
            base_quantity=base_quantity,
            quote_quantity=quote_quantity,
            **kwargs,
        )
        signed_tx = self.operation_wallet.sign_tx(build_res["tx_hex"])
        submit_res = self.orders.submit_place_order_transaction(
            build_res["order_id"], signed_tx, **kwargs
        )
        return submit_res

    def cancel_order(self, order_id: str, **kwargs) -> CancelOrderResponse:
        """
        Cancel an order by its ID.

        Args:
            order_id: The ID of the order to be canceled.

        Returns:
            A CancelOrderResponse containing the canceled order ID.
        """
        return self.orders.cancel_order(order_id, **kwargs)

    def cancel_all_orders(self, symbol: str, **kwargs) -> CancelAllOrdersResponse:
        """
        Cancel all open orders for a given symbol.

        Args:
            symbol: The trading pair symbol (e.g., "ADAUSDM").

        Returns:
            A CancelAllOrdersResponse containing the symbol and canceled order IDs.
        """
        return self.orders.cancel_all_orders(symbol, **kwargs)
