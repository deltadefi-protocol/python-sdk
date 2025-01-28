from typing import Optional, TypedDict


class AuthHeaders(TypedDict, total=False):
    jwt: str
    apiKey: str


class ApiHeaders(TypedDict):
    __annotations__ = {
        "Content-Type": str,
        "Authorization": Optional[str],
        "X-API-KEY": Optional[str]
    }
