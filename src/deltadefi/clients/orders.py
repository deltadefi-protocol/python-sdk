from typing import cast

from deltadefi.api import API
from deltadefi.models.models import OrderSide, OrderType
from deltadefi.responses import (
    BuildCancelAllOrdersTransactionResponse,
    BuildCancelOrderTransactionResponse,
    BuildPlaceOrderTransactionResponse,
    SubmitCancelAllOrdersTransactionResponse,
    SubmitPlaceOrderTransactionResponse,
)
from deltadefi.utils import check_required_parameter, check_required_parameters


class Order(API):
    """
    Orders client for interacting with the DeltaDeFi API.
    """

    group_url_path = "/order"

    def __init__(self, api_key=None, base_url=None, **kwargs):
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)

    def build_place_order_transaction(
        self,
        symbol: str,
        side: OrderSide,
        type: OrderType,
        quantity: int,
        **kwargs,
    ) -> BuildPlaceOrderTransactionResponse:
        """
        Build a place order transaction.

        Args:
            symbol: The trading pair symbol (e.g., "BTC-USD").
            side: The side of the order (e.g., "buy" or "sell").
            type: The type of the order (e.g., "limit" or "market").
            quantity: The quantity of the asset to be traded.
            **kwargs: Additional parameters for the order, such as price, limit_slippage, etc.

        Returns:
            A BuildPlaceOrderTransactionResponse object containing the built order transaction.
        """

        check_required_parameters(
            [
                [symbol, "symbol"],
                [side, "side"],
                [type, "type"],
                [quantity, "quantity"],
            ]
        )

        if type == "limit":
            check_required_parameter(kwargs.get("price"), "price")

        if type == "market" and kwargs.get("limit_slippage"):
            check_required_parameter(
                kwargs.get("max_slippage_basis_point"), "max_slippage_basis_point"
            )

        payload = {
            "symbol": symbol,
            "side": side,
            "type": type,
            "quantity": quantity,
            **kwargs,
        }

        url_path = "/build"
        return cast(
            "BuildPlaceOrderTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def build_cancel_order_transaction(
        self, order_id: str, **kwargs
    ) -> BuildCancelOrderTransactionResponse:
        """
        Build a cancel order transaction.

        Args:
            order_id: The ID of the order to be canceled.

        Returns:
            A BuildCancelOrderTransactionResponse object containing the built cancel order transaction.
        """

        check_required_parameter(order_id, "order_id")

        url_path = f"/{order_id}/build"
        return cast(
            "BuildCancelOrderTransactionResponse",
            self.send_request("DELETE", self.group_url_path + url_path, **kwargs),
        )

    def build_cancel_all_orders_transaction(
        self, **kwargs
    ) -> BuildCancelAllOrdersTransactionResponse:
        """
        Build a cancel all orders transaction.

        Returns:
            A BuildCancelAllOrdersTransactionResponse object containing the built cancel all orders transaction.
        """

        url_path = "/cancel-all/build"
        return cast(
            "BuildCancelAllOrdersTransactionResponse",
            self.send_request("DELETE", self.group_url_path + url_path, **kwargs),
        )

    def submit_place_order_transaction(
        self, order_id: str, signed_tx: str, **kwargs
    ) -> SubmitPlaceOrderTransactionResponse:
        """
        Submit a place order transaction.

        Args:
            order_id: The ID of the order to be placed.
            signed_tx: The signed transaction hex string for placing the order.

        Returns:
            A SubmitPlaceOrderTransactionResponse object containing the submitted order transaction.
        """
        check_required_parameters([[order_id, "order_id"], [signed_tx, "signed_tx"]])
        payload = {"order_id": order_id, "signed_tx": signed_tx, **kwargs}

        url_path = "/submit"
        return cast(
            "SubmitPlaceOrderTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def submit_cancel_order_transaction(self, signed_tx: str, **kwargs):
        """
        Submit a cancel order transaction.

        Args:
            signed_tx: The signed transaction hex string for canceling the order.
        """
        check_required_parameter(signed_tx, "signed_tx")
        payload = {"signed_tx": signed_tx, **kwargs}

        path_url = "/submit"
        return self.send_request("DELETE", self.group_url_path + path_url, payload)

    def submit_cancel_all_orders_transaction(
        self, signed_txs: list[str], **kwargs
    ) -> SubmitCancelAllOrdersTransactionResponse:
        """
        Submit a cancel all orders transaction.

        Args:
            signed_txs: A list of signed transaction hex strings for canceling all orders.
        """
        check_required_parameter(signed_txs, "signed_txs")
        payload = {"signed_txs": signed_txs, **kwargs}

        path_url = "/cancel-all/submit"
        return cast(
            "SubmitCancelAllOrdersTransactionResponse",
            self.send_request("DELETE", self.group_url_path + path_url, payload),
        )
