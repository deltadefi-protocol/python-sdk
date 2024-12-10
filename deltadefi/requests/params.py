from typing import TypedDict, List

class Asset(TypedDict):
    pass # TODO: import Asset

class InputUtxos(TypedDict):
    tx_hash: str
    tx_id: str
    amount: List[Asset]
    address: str