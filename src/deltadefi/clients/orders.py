from typing import Literal, TypedDict

import requests

from deltadefi.requests import (
    BuildPlaceOrderTransactionRequest,
    SubmitCancelOrderTransactionRequest,
    SubmitPlaceOrderTransactionRequest,
)
from deltadefi.responses import (
    BuildCancelOrderTransactionResponse,
    BuildPlaceOrderTransactionResponse,
    SubmitCancelOrderTransactionResponse,
    SubmitPlaceOrderTransactionResponse,
)


class Orders:
    def __init__(self, api_client):
        self.api_client = api_client

    def build_place_order_transaction(
        self, data: BuildPlaceOrderTransactionRequest
    ) -> BuildPlaceOrderTransactionResponse:
        response = requests.post(
            f"{self.api_client.base_url}/order/build",
            json=data,
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def build_cancel_order_transaction(
        self, order_id: str
    ) -> BuildCancelOrderTransactionResponse:
        response = requests.delete(
            f"{self.api_client.base_url}/order/{order_id}/build",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def submit_place_order_transaction(
        self, data: SubmitPlaceOrderTransactionRequest
    ) -> SubmitPlaceOrderTransactionResponse:
        response = requests.post(
            f"{self.api_client.base_url}/order/submit",
            json=data,
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def submit_cancel_order_transaction(
        self, data: SubmitCancelOrderTransactionRequest
    ) -> SubmitCancelOrderTransactionResponse:
        response = requests.delete(
            f"{self.api_client.base_url}/order/submit",
            json=data,
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()
