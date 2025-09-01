from dataclasses import dataclass


@dataclass
class AuthHeaders:
    jwt: str
    api_key: str


class ApiHeaders:
    __annotations__ = {
        "Content-Type": str,
        "Authorization": str | None,
        "X-API-KEY": str | None,
    }
