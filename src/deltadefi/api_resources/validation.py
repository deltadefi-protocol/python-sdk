# flake8: noqa
from dataclasses import dataclass
from typing import List

from sidan_gin import Asset

"""
 * DeltaDeFiOrderInfo is a type that represents the information of a DeltaDeFi order.
 * @property {Asset[]} assetsToPay - The assets that are to be paid from orders in current transaction.
 * @property {Asset[]} assetsToReturn - The assets that are to be received from orders in current transaction.
 * @property {string} txFee - The transaction fee.
 * @property {string} tradingFee - The trading fee.
"""


@dataclass
class DeltaDeFiOrderInfo:
    assetsToPay: List[Asset]
    assetsToReturn: List[Asset]
    txFee: str
    tradingFee: str


"""
 * DeltaDeFiTxInfo is a type that represents the information of a DeltaDeFi transaction.
 * @property {Asset[]} accountInput - The assets that are input from the account.
 * @property {Asset[]} accountOutput - The assets that are output to the account.
 * @property {Asset[]} dexInput - The assets that are input from the DEX.
 * @property {Asset[]} dexOutput - The assets that are output to the DEX.
 * @property {string} txFee - The transaction fee.
 * @property {string} tradingFee - The trading fee.
"""


@dataclass
class DeltaDeFiTxInfo:
    accountInput: List[Asset]
    accountOutput: List[Asset]
    dexInput: List[DeltaDeFiOrderInfo]
    dexOutput: List[DeltaDeFiOrderInfo]
    txFee: str
    tradingFee: str
