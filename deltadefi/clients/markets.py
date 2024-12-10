from typing import TypedDict, Literal
from deltadefi.clients import ApiClient
from deltadefi.responses import GetMarketDepthResponse, GetMarketPriceResponse, GetAggregatedPriceResponse
from deltadefi.requests import GetMarketDepthRequest, GetMarketPriceRequest, GetAggregatedPriceRequest
import requests

class Markets:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def getDepth(self, data: GetMarketDepthRequest) -> GetMarketDepthResponse:
        response = requests.get(
            f"{self.api_client.base_url}/market/depth?pair={data['pair']}",
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()

    def getMarketPrice(self, data: GetMarketPriceRequest) -> GetMarketPriceResponse:
        response = requests.get(
            f"{self.api_client.base_url}/market/market-price?pair={data['pair']}",
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()

    def getAggregatedPrice(self, data: GetAggregatedPriceRequest) -> GetAggregatedPriceResponse:
        response = requests.get(
            f"{self.api_client.base_url}/market/aggregate/{data['pair']}?interval={data['interval']}
            &start={data.get('start', '')}
            &end={data.get('end', '')}",
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()