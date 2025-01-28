from dataclasses import dataclass
from typing import List

from deltadefi.models import OrderJSON


@dataclass
class GetTermsAndConditionResponse:
    value: str


@dataclass
class MarketDepth:
    price: float
    quantity: float


@dataclass
class GetMarketDepthResponse:
    bids: List[MarketDepth]
    asks: List[MarketDepth]


@dataclass
class GetMarketPriceResponse:
    price: float


@dataclass
class Trade:
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
class BuildPlaceOrderTransactionResponse:
    order_id: str
    tx_hex: str


@dataclass
class SubmitPlaceOrderTransactionResponse:
    order: OrderJSON


@dataclass
class PostOrderResponse(SubmitPlaceOrderTransactionResponse):
    pass


@dataclass
class BuildCancelOrderTransactionResponse:
    tx_hex: str


@dataclass
class SubmitCancelOrderTransactionResponse:
    tx_hash: str
