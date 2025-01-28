from dataclasses import dataclass
from typing import Optional

from pycardano import ExtendedSigningKey
from sidan_gin import Network


@dataclass
class ApiConfig:
    network: Optional[Network]
    signingKey: Optional[ExtendedSigningKey]
    jwt: Optional[str]
    apiKey: Optional[str]
