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


@dataclass
class GetOrderRecordResponse(TypedDict):
    order: OrderResponse


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
    id: str
    account_id: str
    to_address: str
    status: str
    transferal_type: str
    assets: list[dict]
    tx_hash: str | None
    created_at: str
    updated_at: str


@dataclass
class GetTransferalRecordsResponse(list[TransferalRecord]):
    pass


@dataclass
class GetTransferalRecordResponse(TypedDict):
    transferal: TransferalRecord


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
