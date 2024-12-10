from typing import TypedDict
from typing_extensions import NotRequired

class AuthHeaders(TypedDict, total=False):
    jwt: str
    apiKey: str

class ApiHeaders(TypedDict):
    'Content-Type': str
    Authorization: NotRequired[str]
    'X-API-KEY': NotRequired[str]