from typing import Literal, TypedDict

TradingSymbol = Literal["ADAUSDX"]

OrderStatus = Literal["building", "open", "closed", "failed"]

OrderSide = Literal["buy", "sell"]

OrderSides = {
    "BuyOrder": "buy",
    "SellOrder": "sell",
}

OrderType = Literal["market", "limit"]

OrderTypes = {
    "MarketOrder": "market",
    "LimitOrder": "limit",
}


class OrderJSON(TypedDict):
    order_id: str
    status: OrderStatus
    symbol: TradingSymbol
    orig_qty: str
    executed_qty: str
    side: OrderSide
    price: str
    type: OrderType
    fee_amount: float
    executed_price: float
    slippage: str
    create_time: int
    update_time: int
