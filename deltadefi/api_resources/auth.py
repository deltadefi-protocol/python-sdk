from typing import TypedDict, Optional

class AuthHeaders(TypedDict, total=False):
    jwt: str
    apiKey: str

class ApiHeaders(TypedDict):
    "Content-Type": str
    Authorization: Optional[str]
    "X-API-KEY": Optional[str]