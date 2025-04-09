# flake8: noqa: E501

from typing import Literal

from deltadefi.api import API
from deltadefi.lib.utils import check_required_parameter, check_required_parameters
from deltadefi.responses import (
    GetAggregatedPriceResponse,
    GetMarketDepthResponse,
    GetMarketPriceResponse,
)


class Market(API):
    """
    Markets client for interacting with the DeltaDeFi API.
    """

    group_url_path = "/market"

    def __init__(self, api_key=None, base_url=None, **kwargs):
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)

    def get_depth(self, symbol: str, **kwargs) -> GetMarketDepthResponse:
        """
        Get market depth.

        Args:
            data: A GetMarketDepthRequest object containing the market pair.

        Returns:
            A GetMarketDepthResponse object containing the market depth.
        """

        check_required_parameter(symbol, "symbol")
        payload = {"symbol": symbol, **kwargs}
        url_path = "/depth"

        return self.send_request("GET", self.group_url_path + url_path, payload)

    def get_market_price(self, symbol: str, **kwargs) -> GetMarketPriceResponse:
        """
        Get market price.

        Args:
            data: A GetMarketPriceRequest object containing the market pair.

        Returns:
            A GetMarketPriceResponse object containing the market price.
        """
        check_required_parameter(symbol, "symbol")
        payload = {"symbol": symbol, **kwargs}
        url_path = "/market-price"
        return self.send_request("GET", self.group_url_path + url_path, payload)

    def get_aggregated_price(
        self,
        symbol: str,
        interval: Literal["15m", "30m", "1h", "1d", "1w", "1M"],
        start: int,
        end: int,
    ) -> GetAggregatedPriceResponse:
        """
        Get aggregated price.

        Args:
            data: A GetAggregatedPriceRequest object containing the market pair, interval, start, and end time.

        Returns:
            A GetAggregatedPriceResponse object containing the aggregated price.
        """

        check_required_parameters(
            [
                [symbol, "symbol"],
                [interval, "interval"],
                [start, "start"],
                [end, "end"],
            ]
        )
        url_path = f"/aggregated-trade/{symbol}"
        return self.send_request(
            "GET",
            self.group_url_path + url_path,
            {
                "interval": interval,
                "start": start,
                "end": end,
            },
        )
