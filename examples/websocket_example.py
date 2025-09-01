"""
Example demonstrating WebSocket client usage for DeltaDeFi real-time data streams.
This file shows how to use all 4 WebSocket endpoints with proper data parsing.
"""

import asyncio
from datetime import datetime
import logging
import os

from dotenv import load_dotenv

from deltadefi import ApiClient

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
api_key = os.getenv("DELTADEFI_API_KEY")

# ============================================================================
# DATA PARSING HANDLERS FOR EACH WEBSOCKET ENDPOINT
# ============================================================================


async def handle_trade_message(data):
    """
    Handle recent trades WebSocket messages.

    Data format: Array of trade objects
    Example: [{"timestamp": "2025-08-21T03:43:00.204624Z", "symbol": "ADAUSDM",
              "side": "sell", "price": 0.7803, "amount": 4.6}, ...]
    """
    print("\n🔄 TRADE STREAM DATA:")
    for i, trade in enumerate(data, 1):
        timestamp = trade.get("timestamp", "")
        symbol = trade.get("symbol", "Unknown")
        side = trade.get("side", "unknown")
        price = trade.get("price", 0)
        amount = trade.get("amount", 0)

        # Convert timestamp to readable format
        try:
            dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            readable_time = dt.strftime("%H:%M:%S")
        except Exception:
            readable_time = timestamp

        side_emoji = "🟢" if side.lower() == "buy" else "🔴"
        print(
            f"  {i}. {side_emoji} {symbol}: {side.upper()} {amount} @ ${price:.4f} at {readable_time}"
        )


async def handle_depth_message(data):
    """
    Handle market depth WebSocket messages.

    Data format: {"timestamp": 1755747950587, "bids": [{"price": 0.195, "quantity": 30}],
                  "asks": [{"price": 0.3495, "quantity": 50.65}]}
    """
    print("\n📊 MARKET DEPTH DATA:")
    timestamp = data.get("timestamp", 0)
    bids = data.get("bids", [])
    asks = data.get("asks", [])

    # Convert timestamp
    try:
        dt = datetime.fromtimestamp(timestamp / 1000)  # Assuming milliseconds
        readable_time = dt.strftime("%H:%M:%S")
    except Exception:
        readable_time = str(timestamp)

    print(f"  📅 Time: {readable_time}")

    # Show top 5 bids and asks
    print("  🟢 BIDS (Buy Orders):")
    for i, bid in enumerate(bids[:5], 1):
        price = bid.get("price", 0)
        quantity = bid.get("quantity", 0)
        print(f"    {i}. ${price:.4f} x {quantity}")

    print("  🔴 ASKS (Sell Orders):")
    for i, ask in enumerate(asks[:5], 1):
        price = ask.get("price", 0)
        quantity = ask.get("quantity", 0)
        print(f"    {i}. ${price:.4f} x {quantity}")

    if bids and asks:
        spread = asks[0]["price"] - bids[0]["price"]
        spread_pct = (spread / bids[0]["price"]) * 100 if bids[0]["price"] > 0 else 0
        print(f"  📈 Spread: ${spread:.4f} ({spread_pct:.3f}%)")


async def handle_price_message(data):
    """
    Handle market price WebSocket messages.

    Data format: {"type": "Market", "sub_type": "market_price", "price": 0.75}
    """
    print("\n💰 PRICE UPDATE:")
    msg_type = data.get("type", "Unknown")
    sub_type = data.get("sub_type", "unknown")
    price = data.get("price", 0)

    print(f"  📊 Type: {msg_type}/{sub_type}")
    print(f"  💵 Current Price: ${price:.4f}")


async def handle_account_message(data):
    """
    Handle account streams WebSocket messages.

    Data formats:
    - Balance: {"type": "Account", "sub_type": "balance", "balance": [...]}
    - Orders: {"type": "Account", "sub_type": "open_orders", "data": [...]}
    """
    msg_type = data.get("type", "Unknown")
    sub_type = data.get("sub_type", "unknown")

    print(f"\n👤 ACCOUNT UPDATE ({msg_type}/{sub_type}):")

    if sub_type == "balance":
        balances = data.get("balance", [])
        print("  💰 Account Balances:")
        for balance in balances:
            asset = balance.get("asset", "unknown")
            free = balance.get("free", 0)
            locked = balance.get("locked", 0)
            total = free + locked

            print(f"    {asset.upper()}: ")
            print(f"      Free: {free:.6f}")
            print(f"      Locked: {locked:.6f}")
            print(f"      Total: {total:.6f}")

    elif sub_type == "open_orders":
        orders_data = data.get("data", [])
        print("  📋 Open Orders:")
        order_count = 0
        for order_group in orders_data:
            orders = order_group.get("orders", [])
            for order in orders:
                order_count += 1
                order_id = order.get("order_id", "unknown")
                status = order.get("status", "unknown")
                symbol = order.get("symbol", "unknown")
                side = order.get("side", "unknown")

                side_emoji = "🟢" if side.lower() == "buy" else "🔴"
                print(
                    f"    {order_count}. {side_emoji} {order_id[:8]}... - {symbol} {side.upper()} ({status})"
                )

        if order_count == 0:
            print("    No open orders")

    elif sub_type == "trading_history":
        print("  📈 Trading History Update")
        print(f"    Data: {data}")

    elif sub_type == "orders_history":
        print("  📜 Orders History Update")
        print(f"    Data: {data}")

    else:
        print(f"  ❓ Unknown sub_type: {sub_type}")
        print(f"    Raw data: {data}")


# ============================================================================
# INDIVIDUAL ENDPOINT EXAMPLES
# ============================================================================


async def example_trades_stream(symbol="ADAUSDM", duration=30):
    """Example: Subscribe to recent trades stream."""
    print(f"\n🚀 Starting TRADES stream for {symbol} (running for {duration}s)")
    print("=" * 60)

    client = ApiClient(api_key=api_key)
    ws_client = client.websocket
    ws_client.register_handler("trade", handle_trade_message)

    try:
        await ws_client.subscribe_trades(symbol)
        print(f"✅ Connected to trades stream for {symbol}")
        await asyncio.sleep(duration)
    except Exception as e:
        print(f"❌ Trades stream error: {e}")
    finally:
        await ws_client.disconnect()


async def example_depth_stream(symbol="ADAUSDM", duration=30):
    """Example: Subscribe to market depth stream."""
    print(f"\n🚀 Starting DEPTH stream for {symbol} (running for {duration}s)")
    print("=" * 60)

    client = ApiClient(api_key=api_key)
    ws_client = client.websocket
    ws_client.register_handler("depth", handle_depth_message)

    try:
        await ws_client.subscribe_depth(symbol)
        print(f"✅ Connected to depth stream for {symbol}")
        await asyncio.sleep(duration)
    except Exception as e:
        print(f"❌ Depth stream error: {e}")
    finally:
        await ws_client.disconnect()


async def example_price_stream(symbol="ADAUSDM", duration=30):
    """Example: Subscribe to market price stream."""
    print(f"\n🚀 Starting PRICE stream for {symbol} (running for {duration}s)")
    print("=" * 60)

    client = ApiClient(api_key=api_key)
    ws_client = client.websocket
    ws_client.register_handler("price", handle_price_message)

    try:
        await ws_client.subscribe_price(symbol)
        print(f"✅ Connected to price stream for {symbol}")
        await asyncio.sleep(duration)
    except Exception as e:
        print(f"❌ Price stream error: {e}")
    finally:
        await ws_client.disconnect()


async def example_account_stream(duration=30):
    """Example: Subscribe to account streams."""
    print(f"\n🚀 Starting ACCOUNT stream (running for {duration}s)")
    print("=" * 60)

    client = ApiClient(api_key=api_key)
    ws_client = client.websocket
    ws_client.register_handler("account", handle_account_message)

    try:
        await ws_client.subscribe_account()
        print("✅ Connected to account stream")
        await asyncio.sleep(duration)
    except Exception as e:
        print(f"❌ Account stream error: {e}")
    finally:
        await ws_client.disconnect()


# ============================================================================
# MAIN FUNCTION WITH ENDPOINT SELECTION
# ============================================================================


async def main():
    """Main function with endpoint selection menu."""
    if not api_key:
        print("❌ Error: DELTADEFI_API_KEY not found in environment variables")
        print("Please set your API key in the .env file")
        return

    print("🔗 DeltaDeFi WebSocket Examples")
    print("=" * 50)
    print("Available endpoints:")
    print("1. Recent Trades Stream")
    print("2. Market Depth Stream")
    print("3. Market Price Stream")
    print("4. Account Streams")
    print("5. Run All Endpoints (Sequential)")
    print("0. Quick Trades Test (10 seconds)")

    try:
        choice = input("\nSelect endpoint (0-5): ").strip()

        if choice == "1":
            await example_trades_stream()
        elif choice == "2":
            await example_depth_stream()
        elif choice == "3":
            await example_price_stream()
        elif choice == "4":
            await example_account_stream()
        elif choice == "5":
            print("\n🔄 Running all endpoints sequentially...")
            await example_trades_stream(duration=15)
            await asyncio.sleep(2)
            await example_depth_stream(duration=15)
            await asyncio.sleep(2)
            await example_price_stream(duration=15)
            await asyncio.sleep(2)
            await example_account_stream(duration=15)
        elif choice == "0":
            await example_trades_stream(duration=10)
        else:
            print("❌ Invalid choice")

    except KeyboardInterrupt:
        print("\n👋 Exiting...")
    except Exception as e:
        print(f"❌ Error: {e}")

    print("\n✅ WebSocket examples completed!")


if __name__ == "__main__":
    asyncio.run(main())
