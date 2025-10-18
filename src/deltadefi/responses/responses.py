from dataclasses import dataclass
from typing import TypedDict

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
    bids: list[MarketDepth]
    asks: list[MarketDepth]


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
class GetAggregatedPriceResponse(list[Trade]):
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


@dataclass
class BuildCancelAllOrdersTransactionResponse(TypedDict):
    tx_hexes: list[str]


@dataclass
class SubmitCancelAllOrdersTransactionResponse(TypedDict):
    cancelled_order_ids: list[str]
