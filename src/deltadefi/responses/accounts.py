from dataclasses import dataclass
from typing import List

from deltadefi.models.models import (
    AssetBalance,
    DepositRecord,
    OrderJSON,
    WithdrawalRecord,
)


@dataclass
class SignInResponse:
    token: str
    is_first_time: bool


@dataclass
class CreateNewAPIKeyResponse:
    api_key: str


@dataclass
class BuildDepositTransactionResponse:
    tx_hex: str


@dataclass
class SubmitDepositTransactionResponse:
    tx_hash: str


@dataclass
class GetDepositRecordsResponse(List[DepositRecord]):
    pass


@dataclass
class GetWithdrawalRecordsResponse(List[WithdrawalRecord]):
    pass


@dataclass
class GetOrderRecordResponse:
    orders: List[OrderJSON]


@dataclass
class BuildWithdrawalTransactionResponse:
    tx_hex: str


@dataclass
class SubmitWithdrawalTransactionResponse:
    tx_hash: str


@dataclass
class GetAccountInfoResponse:
    api_key: str
    api_limit: int
    created_at: str
    updated_at: str


@dataclass
class GetAccountBalanceResponse(List[AssetBalance]):
    pass
