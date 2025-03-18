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
    """
    Orders client for interacting with the DeltaDeFi API.
    """

    def __init__(self, api_client):
        """
        Initialize the Orders client.

        Args:
            api_client: An instance of the ApiClient.
        """
        self.api_client = api_client

    def build_place_order_transaction(
        self, data: BuildPlaceOrderTransactionRequest
    ) -> BuildPlaceOrderTransactionResponse:
        """
        Build a place order transaction.

        Args:
            data: A BuildPlaceOrderTransactionRequest object containing the order details.

        Returns:
            A BuildPlaceOrderTransactionResponse object containing the built order transaction.
        """
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
        """
        Build a cancel order transaction.

        Args:
            order_id: The ID of the order to be canceled.

        Returns:
            A BuildCancelOrderTransactionResponse object containing the built cancel order transaction.
        """
        response = requests.delete(
            f"{self.api_client.base_url}/order/{order_id}/build",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def submit_place_order_transaction(
        self, data: SubmitPlaceOrderTransactionRequest
    ) -> SubmitPlaceOrderTransactionResponse:
        """
        Submit a place order transaction.

        Args:
            data: A SubmitPlaceOrderTransactionRequest object containing the order details.

        Returns:
            A SubmitPlaceOrderTransactionResponse object containing the submitted order transaction.
        """
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
        """
        Submit a cancel order transaction.

        Args:
            data: A SubmitCancelOrderTransactionRequest object containing the cancel order details.

        Returns:
            A SubmitCancelOrderTransactionResponse object containing the submitted cancel order transaction.
        """
        response = requests.delete(
            f"{self.api_client.base_url}/order/submit",
            json=data,
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()
