from typing import cast

from deltadefi.api import API
from deltadefi.responses.app import (
    GetHydraCycleResponse,
    GetMarketConfigResponse,
    GetMockUsdxResponse,
    GetTermsAndConditionsResponse,
    SubmitTxResponse,
)
from deltadefi.utils import check_required_parameter


class App(API):
    """
    App client for interacting with the DeltaDeFi API.

    Provides access to application-level endpoints like market configuration,
    Hydra cycle information, and transaction submission.
    """

    group_url_path = "/app"

    def __init__(self, api_key=None, base_url=None, **kwargs):
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)

    def get_terms_and_conditions(self, **kwargs) -> GetTermsAndConditionsResponse:
        """
        Get the terms and conditions.

        Returns:
            A GetTermsAndConditionsResponse object containing the terms and conditions.
        """
        url_path = "/terms-and-conditions"
        return cast(
            "GetTermsAndConditionsResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_hydra_cycle(self, **kwargs) -> GetHydraCycleResponse:
        """
        Get the current Hydra cycle timing information.

        Returns:
            A GetHydraCycleResponse object containing start and end timestamps.
        """
        url_path = "/hydra-cycle"
        return cast(
            "GetHydraCycleResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_market_config(self, **kwargs) -> GetMarketConfigResponse:
        """
        Get the market configuration including trading pairs and assets.

        Returns:
            A GetMarketConfigResponse object containing trading pair and asset configs.
        """
        url_path = "/market-config"
        return cast(
            "GetMarketConfigResponse",
            self.send_request("GET", self.group_url_path + url_path, kwargs),
        )

    def get_mock_usdx(self, **kwargs) -> GetMockUsdxResponse:
        """
        Get mock USDX tokens (testnet only).

        Returns:
            A GetMockUsdxResponse object containing the signed transaction and tx hash.
        """
        url_path = "/mock-usdx"
        return cast(
            "GetMockUsdxResponse",
            self.send_request("POST", self.group_url_path + url_path, kwargs),
        )

    def submit_tx(self, signed_tx: str, **kwargs) -> SubmitTxResponse:
        """
        Submit a signed transaction to the network.

        Args:
            signed_tx: The signed transaction hex string.

        Returns:
            A SubmitTxResponse object containing the transaction hash.
        """
        check_required_parameter(signed_tx, "signed_tx")
        payload = {"signed_tx": signed_tx, **kwargs}

        url_path = "/submit-tx"
        return cast(
            "SubmitTxResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )
