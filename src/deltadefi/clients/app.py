import requests

from deltadefi.responses import GetTermsAndConditionResponse


class App:
    def __init__(self, api_client):
        self.api_client = api_client

    def getTermsAndCondition(self) -> GetTermsAndConditionResponse:
        response = requests.get(
            f"{self.api_client.base_url}/terms-and-conditions",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()
