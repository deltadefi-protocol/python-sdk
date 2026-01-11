from dataclasses import dataclass
from typing import TypedDict


@dataclass
class GetTermsAndConditionsResponse(TypedDict):
    """Response for GET /app/terms-and-conditions"""

    value: str


@dataclass
class GetHydraCycleResponse(TypedDict):
    """Response for GET /app/hydra-cycle"""

    start: str
    end: str


@dataclass
class MarketConfigToken(TypedDict):
    """Token information within a trading pair"""

    symbol: str
    unit: str
    decimals: int
    max_qty_dp: int


@dataclass
class MarketConfigTradingPair(TypedDict):
    """Trading pair configuration"""

    symbol: str
    base_token: MarketConfigToken
    quote_token: MarketConfigToken
    price_max_dp: int


@dataclass
class MarketConfigAsset(TypedDict):
    """Asset information for client display and validation"""

    symbol: str
    unit: str
    decimals: int
    max_qty_dp: int
    trading_pairs: list[str]


@dataclass
class GetMarketConfigResponse(TypedDict):
    """Response for GET /app/market-config"""

    trading_pairs: list[MarketConfigTradingPair]
    assets: list[MarketConfigAsset]


@dataclass
class GetMockUsdxResponse(TypedDict):
    """Response for POST /app/mock-usdx"""

    signed_tx: str
    tx_hash: str


@dataclass
class SubmitTxResponse(TypedDict):
    """Response for POST /app/submit-tx"""

    tx_hash: str
