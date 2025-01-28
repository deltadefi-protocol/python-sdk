from typing import Literal, Optional, TypedDict

from pycardano import ExtendedSigningKey
from sidan_gin import Network


class ApiConfig(TypedDict, total=False):
    network: Optional[Network]
    signingKey: Optional[ExtendedSigningKey]
    jwt: Optional[str]
    apiKey: Optional[str]
