from dataclasses import dataclass
from typing import Literal, TypedDict

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

OrderExecutionRole = Literal["maker", "taker"]


@dataclass
class AssetRecord:
    asset: str
    asset_unit: str
    qty: str


@dataclass
class TransactionStatus:
    building = "building"
    held_for_order = "held_for_order"
    submitted = "submitted"
    submission_failed = "submission_failed"
    confirmed = "confirmed"


class OrderExecutionRecordResponse(TypedDict):
    """Order execution record representing a single trade execution."""

    id: str
    order_id: str
    account_id: str
    execution_price: str
    filled_base_qty: str
    filled_quote_qty: str
    commission_unit: str
    commission: str
    role: OrderExecutionRole
    counter_party_order_id: str
    created_at: str


class OrderResponse(TypedDict):
    """Order response with quantities in human-readable format."""

    id: str
    account_id: str
    active_order_utxo_id: str | None
    status: OrderStatus
    symbol: str
    base_qty: str
    quote_qty: str
    side: OrderSide
    price: str
    type: OrderType
    slippage_bp: int | None
    market_order_limit_price: str | None
    locked_base_qty: str
    locked_quote_qty: str
    executed_base_qty: str
    executed_quote_qty: str
    ob_open_order_base_qty: str
    commission_unit: str
    commission: str
    commission_rate_bp: int
    executed_price: str
    created_at: str
    updated_at: str
    order_execution_records: list[OrderExecutionRecordResponse] | None


# Deprecated: Use OrderResponse instead
@dataclass
class OrderJSON:
    """Deprecated: Use OrderResponse instead."""

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
    assets: list[AssetRecord]
    tx_hash: str


@dataclass
class WithdrawalRecord:
    created_at: str
    status: TransactionStatus
    assets: list[AssetRecord]


@dataclass
class AssetBalance:
    asset: str
    asset_unit: str
    free: str
    locked: str


# Deprecated: Use OrderExecutionRecordResponse instead
@dataclass
class OrderFillingRecordJSON:
    """Deprecated: Use OrderExecutionRecordResponse instead."""

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
