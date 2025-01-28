from enum import Enum
from typing import List, TypedDict

from sidan_gin import Asset

from deltadefi.models import OrderJSON


class SignInResponse(TypedDict):
    token: str
    is_ready: bool


class TransactionStatus(str, Enum):
    building = "building"
    held_for_order = "held_for_order"
    submitted = "submitted"
    submission_failed = "submission_failed"
    confirmed = "confirmed"


class DepositRecord(TypedDict):
    created_at: str
    status: TransactionStatus
    assets: List[Asset]
    tx_hash: str


class GetDepositRecordsResponse(List[DepositRecord]):
    pass


class GetOrderRecordResponse(TypedDict):
    Orders: List[OrderJSON]


class WithdrawalRecord(TypedDict):
    created_at: str
    assets: List[Asset]


class GetWithdrawalRecordsResponse(List[WithdrawalRecord]):
    pass


class AssetBalance(TypedDict):
    asset: str
    free: int
    locked: int


class GetAccountBalanceResponse(List[AssetBalance]):
    pass


class GenerateNewAPIKeyResponse(TypedDict):
    api_key: str


class BuildDepositTransactionResponse(TypedDict):
    tx_hex: str


class BuildWithdrawalTransactionResponse(TypedDict):
    tx_hex: str


class SubmitDepositTransactionResponse(TypedDict):
    tx_hash: str


class SubmitWithdrawalTransactionResponse(TypedDict):
    tx_hash: str


class GetTermsAndConditionResponse(TypedDict):
    value: str


class MarketDepth(TypedDict):
    price: float
    quantity: float


class GetMarketDepthResponse(TypedDict):
    bids: List[MarketDepth]
    asks: List[MarketDepth]


class GetMarketPriceResponse(TypedDict):
    price: float


class Trade(TypedDict):
    time: str
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: float


class GetAggregatedPriceResponse(List[Trade]):
    pass


class BuildPlaceOrderTransactionResponse(TypedDict):
    order_id: str
    tx_hex: str


class SubmitPlaceOrderTransactionResponse(TypedDict):
    order: OrderJSON


class PostOrderResponse(SubmitPlaceOrderTransactionResponse):
    pass


class BuildCancelOrderTransactionResponse(TypedDict):
    tx_hex: str


class SubmitCancelOrderTransactionResponse(TypedDict):
    tx_hash: str
