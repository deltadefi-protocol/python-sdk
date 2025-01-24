from typing import TypedDict, List
from sidan_gin import Asset

class InputUtxos(TypedDict):
    tx_hash: str
    tx_id: str
    amount: List[Asset]
    address: str