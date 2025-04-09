from deltadefi.api import API
from deltadefi.responses import GetTermsAndConditionResponse


class App(API):
    """
    App client for interacting with the DeltaDeFi API.
    """

    group_url_path = "/app"

    def __init__(self, api_key=None, base_url=None, **kwargs):
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)

    def get_terms_and_condition(self, **kwargs) -> GetTermsAndConditionResponse:
        """
        Get terms and conditions.

        Returns:
            A GetTermsAndConditionResponse object containing the terms and conditions.
        """
        url_path = "/terms-and-conditions"
        return self.send_request("GET", self.group_url_path + url_path, kwargs)
