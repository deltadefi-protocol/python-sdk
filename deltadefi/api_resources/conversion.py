from typing import TypedDict, List
from deltadefi.requests.params import InputUtxos

class Asset(TypedDict): 
    pass # TODO: import Asset

class UTxO(TypedDict): # TODO: import UTxO
    pass

class TxInParameter(TypedDict): # TODO: import TxInParameter
    txHash: str
    txIndex: int
    amount: List[Asset]
    address: str

def convert_utxo(utxo: UTxO) -> InputUtxos:
    return {
        'tx_hash': utxo['input']['txHash'],
        'tx_id': str(utxo['input']['outputIndex']),
        'amount': utxo['output']['amount'],
        'address': utxo['output']['address']
    }

def convert_utxos(utxos: List[UTxO]) -> List[InputUtxos]:
    return [convert_utxo(utxo) for utxo in utxos]

def convert_tx_in_parameter(tx_in: TxInParameter) -> InputUtxos:
    return {
        'tx_hash': tx_in['txHash'],
        'tx_id': str(tx_in['txIndex']),
        'amount': tx_in.get('amount', []),
        'address': tx_in.get('address', '')
    }