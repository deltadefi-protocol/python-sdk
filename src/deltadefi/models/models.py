from dataclasses import dataclass
from typing import List, Literal

OrderStatusType = Literal["openOrder", "orderHistory", "tradingHistory"]

OrderStatus = Literal[
    "open", "fully_filled", "partially_filled", "cancelled", "partially_cancelled"
]

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
class AssetRecord:
    asset: str
    asset_unit: str
    qty: float


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
    symbol: str
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
    assets: List[AssetRecord]
    tx_hash: str


@dataclass
class WithdrawalRecord:
    created_at: str
    status: TransactionStatus
    assets: List[AssetRecord]


@dataclass
class AssetBalance:
    asset: str
    free: int
    locked: int


@dataclass
class OrderFillingRecordJSON:
    execution_id: str
    order_id: str
    status: OrderStatus
    symbol: str
    executed_qty: str
    side: OrderSide
    type: OrderType
    fee_charged: str
    fee_unit: str
    executed_price: float
    created_time: int
