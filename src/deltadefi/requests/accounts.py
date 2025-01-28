from dataclasses import dataclass
from typing import List

from sidan_gin import Asset, UTxO


@dataclass
class SignInRequest:
    wallet_address: str
    auth_key: str


@dataclass
class BuildDepositTransactionRequest:
    deposit_amount: List[Asset]
    input_utxos: List[UTxO]


class BuildWithdrawalTransactionRequest:
    withdrawal_amount: List[Asset]


class SubmitDepositTransactionRequest:
    signed_tx: str


class SubmitWithdrawalTransactionRequest:
    signed_txs: List[str]
