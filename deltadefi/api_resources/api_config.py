from typing import TypedDict, Literal
from typing_extensions import NotRequired

class AppWalletKeyType(str):
    pass # TODO: import AppWalletKeyType

class ApiConfig(TypedDict, total=False):
    network: NotRequired[Literal['preprod', 'mainnet']]
    signingKey: NotRequired[AppWalletKeyType]
    jwt: NotRequired[str]
    apiKey: NotRequired[str]