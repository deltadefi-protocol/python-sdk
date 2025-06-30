from dataclasses import dataclass
from typing import List, TypedDict

from deltadefi.models.models import (
    AssetBalance,
    DepositRecord,
    OrderFillingRecordJSON,
    OrderJSON,
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
class GetDepositRecordsResponse(List[DepositRecord]):
    pass


@dataclass
class GetWithdrawalRecordsResponse(List[WithdrawalRecord]):
    pass


@dataclass
class GetOrderRecordResponse(TypedDict):
    orders: List[OrderJSON]
    order_filling_records: List[OrderFillingRecordJSON]


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
class GetAccountBalanceResponse(List[AssetBalance]):
    pass
