import requests

from deltadefi.responses import GetTermsAndConditionResponse


class App:
    """
    App client for interacting with the DeltaDeFi API.
    """

    def __init__(self, api_client):
        """
        Initialize the App client.

        Args:
            api_client: An instance of the ApiClient.
        """
        self.api_client = api_client

    def getTermsAndCondition(self) -> GetTermsAndConditionResponse:
        """
        Get terms and conditions.

        Returns:
            A GetTermsAndConditionResponse object containing the terms and conditions.
        """
        response = requests.get(
            f"{self.api_client.base_url}/terms-and-conditions",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()
