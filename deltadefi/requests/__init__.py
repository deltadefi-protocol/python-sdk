from typing import TypedDict, List, Literal
from deltadefi.models import TradingSymbol, OrderSide, OrderType
from typing_extensions import NotRequired

class Asset(TypedDict): 
    pass # TODO: import Asset

class UTxO(TypedDict): # TODO: import UTxO
    pass

class SignInRequest(TypedDict):
    wallet_address: str
    auth_key: str

class BuildDepositTransactionRequest(TypedDict):
    deposit_amount: List[Asset]
    input_utxos: List[UTxO]

class BuildWithdrawalTransactionRequest(TypedDict):
    withdrawal_amount: List[Asset]

class SubmitDepositTransactionRequest(TypedDict):
    signed_tx: str

class SubmitWithdrawalTransactionRequest(TypedDict):
    signed_txs: List[str]

class GetMarketDepthRequest(TypedDict):
    pair: str

class GetMarketPriceRequest(TypedDict):
    pair: str

Interval = Literal['15m', '30m', '1h', '1d', '1w', '1M']

class GetAggregatedPriceRequest(TypedDict, total=False):
    pair: str
    interval: Interval
    start: NotRequired[int]
    end: NotRequired[int]

class TradingSymbol(str):
    pass

class OrderSide(str):
    pass

class OrderType(str):
    pass

class BuildPlaceOrderTransactionRequest(TypedDict):
    pair: TradingSymbol
    side: OrderSide
    type: OrderType
    quantity: float
    price: NotRequired[float]
    basis_point: NotRequired[float]

class PostOrderRequest(BuildPlaceOrderTransactionRequest):
    pass

class SubmitPlaceOrderTransactionRequest(TypedDict):
    order_id: str
    signed_tx: str

class BuildCancelOrderTransactionRequest(TypedDict):
    order_id: str

class SubmitCancelOrderTransactionRequest(TypedDict):
    signed_tx: str