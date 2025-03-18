# flake8: noqa: E501

import requests

from deltadefi.requests import (
    GetAggregatedPriceRequest,
    GetMarketDepthRequest,
    GetMarketPriceRequest,
)
from deltadefi.responses import (
    GetAggregatedPriceResponse,
    GetMarketDepthResponse,
    GetMarketPriceResponse,
)


class Markets:
    """
    Markets client for interacting with the DeltaDeFi API.
    """

    def __init__(self, api_client):
        """
        Initialize the Markets client.

        Args:
            api_client: An instance of the ApiClient.
        """
        self.api_client = api_client

    def getDepth(self, data: GetMarketDepthRequest) -> GetMarketDepthResponse:
        """
        Get market depth.

        Args:
            data: A GetMarketDepthRequest object containing the market pair.

        Returns:
            A GetMarketDepthResponse object containing the market depth.
        """
        response = requests.get(
            f"{self.api_client.base_url}/market/depth?pair={data['pair']}",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def getMarketPrice(self, data: GetMarketPriceRequest) -> GetMarketPriceResponse:
        """
        Get market price.

        Args:
            data: A GetMarketPriceRequest object containing the market pair.

        Returns:
            A GetMarketPriceResponse object containing the market price.
        """
        response = requests.get(
            f"{self.api_client.base_url}/market/market-price?pair={data['pair']}",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def getAggregatedPrice(
        self, data: GetAggregatedPriceRequest
    ) -> GetAggregatedPriceResponse:
        """
        Get aggregated price.

        Args:
            data: A GetAggregatedPriceRequest object containing the market pair, interval, start, and end time.

        Returns:
            A GetAggregatedPriceResponse object containing the aggregated price.
        """
        response = requests.get(
            f"{self.api_client.base_url}/market/aggregate/{data['pair']}?interval={data['interval']}&start={data.get('start', '')}&end={data.get('end', '')}",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()
