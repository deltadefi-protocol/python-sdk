from typing import cast

from deltadefi.api import API
from deltadefi.models.models import OrderSide, OrderType
from deltadefi.responses import (
    BuildPlaceOrderTransactionResponse,
    CancelAllOrdersResponse,
    CancelOrderResponse,
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
        base_quantity: str | None = None,
        quote_quantity: str | None = None,
        **kwargs,
    ) -> BuildPlaceOrderTransactionResponse:
        """
        Build a place order transaction.

        Args:
            symbol: The trading pair symbol (e.g., "ADAUSDM").
            side: The side of the order ("buy" or "sell").
            type: The type of the order ("limit" or "market").
            base_quantity: The quantity in base asset (e.g., ADA). Mutually exclusive with quote_quantity.
            quote_quantity: The quantity in quote asset (e.g., USDM). Mutually exclusive with base_quantity.
            price: Required for limit orders; The price for the order.
            max_slippage_basis_point: Optional; The maximum slippage in basis points for market orders.
            post_only: Optional; If True, the order will only be placed if it would be a maker order.

        Returns:
            A BuildPlaceOrderTransactionResponse object containing the built order transaction.
        """

        check_required_parameters(
            [
                [symbol, "symbol"],
                [side, "side"],
                [type, "type"],
            ]
        )

        # Validate that exactly one of base_quantity or quote_quantity is provided
        if base_quantity is None and quote_quantity is None:
            raise ValueError("Either base_quantity or quote_quantity must be provided")
        if base_quantity is not None and quote_quantity is not None:
            raise ValueError(
                "Only one of base_quantity or quote_quantity can be provided, not both"
            )

        if type == "limit":
            check_required_parameter(kwargs.get("price"), "price")

        payload = {
            "symbol": symbol,
            "side": side,
            "type": type,
            **kwargs,
        }

        if base_quantity is not None:
            payload["base_quantity"] = base_quantity
        if quote_quantity is not None:
            payload["quote_quantity"] = quote_quantity

        url_path = "/build"
        return cast(
            "BuildPlaceOrderTransactionResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
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

    def cancel_order(self, order_id: str, **kwargs) -> CancelOrderResponse:
        """
        Cancel an order by its ID.

        Args:
            order_id: The ID of the order to be canceled.

        Returns:
            A CancelOrderResponse object containing the canceled order ID.
        """
        check_required_parameter(order_id, "order_id")
        payload = {"order_id": order_id, **kwargs}

        url_path = f"/{order_id}/cancel"
        return cast(
            "CancelOrderResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )

    def cancel_all_orders(self, symbol: str, **kwargs) -> CancelAllOrdersResponse:
        """
        Cancel all open orders for a given symbol.

        Args:
            symbol: The trading pair symbol (e.g., "ADAUSDM").

        Returns:
            A CancelAllOrdersResponse object containing the symbol and canceled order IDs.
        """
        check_required_parameter(symbol, "symbol")
        payload = {"symbol": symbol, **kwargs}

        url_path = "/cancel-all"
        return cast(
            "CancelAllOrdersResponse",
            self.send_request("POST", self.group_url_path + url_path, payload),
        )
