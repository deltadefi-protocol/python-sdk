from dataclasses import dataclass
from typing import List, Literal

from sidan_gin import Asset

TradingSymbol = Literal["ADAUSDX"]

OrderStatus = Literal["building", "open", "closed", "failed"]

OrderSide = Literal["buy", "sell"]

OrderSides = {
    "BuyOrder": "buy",
    "SellOrder": "sell",
}

OrderType = Literal["market", "limit"]

OrderTypes = {
    "MarketOrder": "market",
    "LimitOrder": "limit",
}


@dataclass
class TransactionStatus:
    building = "building"
    held_for_order = "held_for_order"
    submitted = "submitted"
    submission_failed = "submission_failed"
    confirmed = "confirmed"


@dataclass
class OrderJSON:
    order_id: str
    status: OrderStatus
    symbol: TradingSymbol
    orig_qty: str
    executed_qty: str
    side: OrderSide
    price: str
    type: OrderType
    fee_amount: float
    executed_price: float
    slippage: str
    create_time: int
    update_time: int


@dataclass
class DepositRecord:
    created_at: str
    status: TransactionStatus
    assets: List[Asset]
    tx_hash: str


@dataclass
class WithdrawalRecord:
    created_at: str
    status: TransactionStatus
    assets: List[Asset]


@dataclass
class AssetBalance:
    asset: str
    free: int
    locked: int
