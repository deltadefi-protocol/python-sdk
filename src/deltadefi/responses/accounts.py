from dataclasses import dataclass
from typing import TypedDict

from deltadefi.models.models import (
    AssetBalance,
    DepositRecord,
    OrderExecutionRecordResponse,
    OrderFillingRecordJSON,
    OrderJSON,
    OrderResponse,
    WithdrawalRecord,
)


@dataclass
class CreateNewAPIKeyResponse(TypedDict):
    api_key: str
    created_at: str


@dataclass
class GetOperationKeyResponse(TypedDict):
    encrypted_operation_key: str
    operation_key_hash: str


@dataclass
class BuildDepositTransactionResponse(TypedDict):
    tx_hex: str


@dataclass
class SubmitDepositTransactionResponse(TypedDict):
    tx_hash: str


@dataclass
class GetDepositRecordsResponse(list[DepositRecord]):
    pass


@dataclass
class GetWithdrawalRecordsResponse(list[WithdrawalRecord]):
    pass


# Deprecated: Use get_open_orders, get_trade_orders, or get_trades instead
@dataclass
class OrderRecordsData(TypedDict):
    orders: list[OrderJSON]
    order_filling_records: list[OrderFillingRecordJSON]


# Deprecated: Use get_open_orders, get_trade_orders, or get_trades instead
@dataclass
class GetOrderRecordsResponse(TypedDict):
    data: list[OrderRecordsData]
    total_count: int
    total_page: int


# GetOrderRecordResponse returns OrderResponse directly (not wrapped)
GetOrderRecordResponse = OrderResponse


@dataclass
class BuildWithdrawalTransactionResponse(TypedDict):
    tx_hex: str


@dataclass
class BuildTransferalTransactionResponse(TypedDict):
    tx_hex: str


@dataclass
class SubmitWithdrawalTransactionResponse(TypedDict):
    tx_hash: str


@dataclass
class SubmitTransferalTransactionResponse(TypedDict):
    tx_hash: str


@dataclass
class GetAccountInfoResponse(TypedDict):
    api_key: str
    api_limit: int
    created_at: str
    updated_at: str


@dataclass
class GetAccountBalanceResponse(list[AssetBalance]):
    pass


# New response types for espresso develop branch


@dataclass
class BuildRequestTransferalTransactionResponse(TypedDict):
    tx_hex: str


@dataclass
class SubmitRequestTransferalTransactionResponse(TypedDict):
    tx_hash: str


@dataclass
class GetSpotAccountResponse(TypedDict):
    account_id: str
    account_type: str
    encrypted_operation_key: str
    operation_key_hash: str
    created_at: str


@dataclass
class CreateSpotAccountResponse(TypedDict):
    account_id: str
    account_type: str
    encrypted_operation_key: str
    operation_key_hash: str
    created_at: str


@dataclass
class UpdateSpotAccountResponse(TypedDict):
    account_id: str
    account_type: str
    encrypted_operation_key: str
    operation_key_hash: str
    created_at: str
    updated_at: str


@dataclass
class TransferalRecord(TypedDict):
    created_at: str
    status: str  # "pending" or "confirmed"
    assets: list[dict]
    transferal_type: str
    tx_hash: str
    direction: str  # "incoming" or "outgoing"


@dataclass
class GetTransferalRecordsResponse(list[TransferalRecord]):
    pass


# GetTransferalRecordResponse returns TransferalRecord directly (not wrapped)
GetTransferalRecordResponse = TransferalRecord


@dataclass
class GetAPIKeyResponse(TypedDict):
    api_key: str
    created_at: str


@dataclass
class GetMaxDepositResponse(TypedDict):
    max_deposit: str


@dataclass
class GetOpenOrdersResponse(list[OrderResponse]):
    pass


@dataclass
class GetTradeOrdersResponse(list[OrderResponse]):
    pass


@dataclass
class GetTradesResponse(list[OrderExecutionRecordResponse]):
    pass
