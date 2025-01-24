from typing import TypedDict, Literal, Optional
from sidan_gin import Network
from pycardano import ExtendedSigningKey

class ApiConfig(TypedDict, total=False):
    network: Optional[Network]
    signingKey: Optional[ExtendedSigningKey]
    jwt: Optional[str]
    apiKey: Optional[str]