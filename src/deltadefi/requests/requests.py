from typing import Literal, Optional, TypedDict

from deltadefi.models import OrderSide, OrderType, TradingSymbol


class GetMarketDepthRequest(TypedDict):
    pair: str


class GetMarketPriceRequest(TypedDict):
    pair: str


Interval = Literal["15m", "30m", "1h", "1d", "1w", "1M"]


class GetAggregatedPriceRequest(TypedDict, total=False):
    pair: str
    interval: Interval
    start: Optional[int]
    end: Optional[int]


# class TradingSymbol(str):
#     pass


# class OrderSide(str):
#     pass


# class OrderType(str):
#     pass


class BuildPlaceOrderTransactionRequest(TypedDict):
    pair: TradingSymbol
    side: OrderSide
    type: OrderType
    quantity: float
    price: Optional[float]
    basis_point: Optional[float]


class PostOrderRequest(BuildPlaceOrderTransactionRequest):
    pass


class SubmitPlaceOrderTransactionRequest(TypedDict):
    order_id: str
    signed_tx: str


class BuildCancelOrderTransactionRequest(TypedDict):
    order_id: str


class SubmitCancelOrderTransactionRequest(TypedDict):
    signed_tx: str
