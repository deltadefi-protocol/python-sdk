from dataclasses import dataclass
from typing import List, TypedDict

from deltadefi.models import OrderJSON


@dataclass
class GetTermsAndConditionResponse(TypedDict):
    value: str


@dataclass
class MarketDepth(TypedDict):
    price: float
    quantity: float


@dataclass
class GetMarketDepthResponse(TypedDict):
    bids: List[MarketDepth]
    asks: List[MarketDepth]


@dataclass
class GetMarketPriceResponse(TypedDict):
    price: float


@dataclass
class Trade(TypedDict):
    time: str
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass
class GetAggregatedPriceResponse(List[Trade]):
    pass


@dataclass
class BuildPlaceOrderTransactionResponse(TypedDict):
    order_id: str
    tx_hex: str


@dataclass
class SubmitPlaceOrderTransactionResponse(TypedDict):
    order: OrderJSON


@dataclass
class PostOrderResponse(SubmitPlaceOrderTransactionResponse):
    pass


@dataclass
class BuildCancelOrderTransactionResponse(TypedDict):
    tx_hex: str
