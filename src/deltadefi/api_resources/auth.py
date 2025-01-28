from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthHeaders:
    jwt: str
    apiKey: str


class ApiHeaders:
    __annotations__ = {
        "Content-Type": str,
        "Authorization": Optional[str],
        "X-API-KEY": Optional[str],
    }
