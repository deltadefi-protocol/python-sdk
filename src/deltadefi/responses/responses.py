from dataclasses import dataclass
from typing import TypedDict

from deltadefi.models import OrderResponse


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


# SubmitPlaceOrderTransactionResponse returns OrderResponse directly (not wrapped)
SubmitPlaceOrderTransactionResponse = OrderResponse

# PostOrderResponse is an alias for SubmitPlaceOrderTransactionResponse
PostOrderResponse = SubmitPlaceOrderTransactionResponse


@dataclass
class CancelOrderResponse(TypedDict):
    order_id: str


@dataclass
class CancelAllOrdersResponse(TypedDict):
    symbol: str
    order_ids: list[str]
