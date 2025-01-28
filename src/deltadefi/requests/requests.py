from dataclasses import dataclass
from typing import Literal, Optional

from deltadefi.models import OrderSide, OrderType, TradingSymbol


@dataclass
class GetMarketDepthRequest:
    pair: str


@dataclass
class GetMarketPriceRequest:
    pair: str


Interval = Literal["15m", "30m", "1h", "1d", "1w", "1M"]


@dataclass
class GetAggregatedPriceRequest:
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


@dataclass
class BuildPlaceOrderTransactionRequest:
    pair: TradingSymbol
    side: OrderSide
    type: OrderType
    quantity: float
    price: Optional[float]
    basis_point: Optional[float]


class PostOrderRequest(BuildPlaceOrderTransactionRequest):
    pass


@dataclass
class SubmitPlaceOrderTransactionRequest:
    order_id: str
    signed_tx: str


@dataclass
class BuildCancelOrderTransactionRequest:
    order_id: str


@dataclass
class SubmitCancelOrderTransactionRequest:
    signed_tx: str
