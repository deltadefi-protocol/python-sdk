# flake8: noqa: E501
from sidan_gin import Wallet, decrypt_with_cipher

from deltadefi.clients.accounts import Accounts
from deltadefi.clients.app import App
from deltadefi.clients.markets import Market
from deltadefi.clients.orders import Order
from deltadefi.models.models import OrderSide, OrderType
from deltadefi.responses import PostOrderResponse


class ApiClient:
    """
    ApiClient for interacting with the DeltaDeFi API.
    """

    def __init__(
        self,
        network: str = "preprod",
        api_key: str = None,
        base_url: str = None,
        master_wallet: Wallet = None,
    ):
        """
        Initialize the ApiClient.

        Args:
            config: An instance of ApiConfig containing the API configuration.
            wallet: An instance of Wallet for signing transactions.
            base_url: Optional; The base URL for the API. Defaults to "https://api-dev.deltadefi.io".
        """
        if network == "mainnet":
            self.network_id = 1
            self.base_url = "https://api-dev.deltadefi.io"  # TODO: input production link once available
        else:
            self.network_id = 0
            self.base_url = "https://api-staging.deltadefi.io"

        if base_url:
            self.base_url = base_url

        self.api_key = api_key
        self.master_wallet = master_wallet

        self.accounts = Accounts(base_url=self.base_url, api_key=api_key)
        self.app = App(base_url=self.base_url, api_key=api_key)
        self.orders = Order(base_url=self.base_url, api_key=api_key)
        self.markets = Market(base_url=self.base_url, api_key=api_key)

    def load_operation_key(self, password: str):
        """
        Load the operation key from the wallet using the provided password.

        Args:
            password: The password to decrypt the operation key.

        Returns:
            The decrypted operation key.
        """
        res = self.accounts.get_operation_key()
        operation_key = decrypt_with_cipher(res["encrypted_operation_key"], password)
        self.operation_wallet = Wallet.new_root_key(operation_key)

    def post_order(
        self, symbol: str, side: OrderSide, type: OrderType, quantity: int, **kwargs
    ) -> PostOrderResponse:
        """
        Post an order to the DeltaDeFi API. It includes building the transaction, signing it with the wallet, and submitting it.

        Args:
            symbol: The trading pair symbol (e.g., "BTC-USD").
            side: The side of the order (e.g., "buy" or "sell").
            type: The type of the order (e.g., "limit" or "market").
            quantity: The quantity of the asset to be traded.
            price: Required for limit order; The price for limit orders.
            limit_slippage: Optional; Whether to apply slippage for market orders. Defaults to False.
            max_slippage_basis_point: Optional; The maximum slippage in basis points for market orders. Defaults to null.

        Returns:
            A PostOrderResponse object containing the response from the API.

        Raises:
            ValueError: If the wallet is not initialized.
        """
        if not hasattr(self, "operation_wallet") or self.operation_wallet is None:
            raise ValueError("Operation wallet is not initialized")

        build_res = self.orders.build_place_order_transaction(
            symbol, side, type, quantity, **kwargs
        )
        signed_tx = self.operation_wallet.sign_tx(build_res["tx_hex"])
        submit_res = self.orders.submit_place_order_transaction(
            build_res["order_id"], signed_tx, **kwargs
        )
        return submit_res

    def cancel_order(self, order_id: str, **kwargs):
        """
        Cancel an order by its ID.

        Args:
            order_id: The ID of the order to be canceled.
        """
        if not hasattr(self, "operation_wallet") or self.operation_wallet is None:
            raise ValueError("Operation wallet is not initialized")

        build_res = self.orders.build_cancel_order_transaction(order_id)
        signed_tx = self.operation_wallet.sign_tx(build_res["tx_hex"])
        self.orders.submit_cancel_order_transaction(signed_tx, **kwargs)
        return {"message": "Order cancelled successfully", "order_id": order_id}
