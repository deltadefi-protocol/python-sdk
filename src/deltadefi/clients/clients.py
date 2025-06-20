# flake8: noqa: E501
from sidan_gin import Wallet

from deltadefi.clients.accounts import Accounts
from deltadefi.clients.app import App
from deltadefi.clients.market import Market
from deltadefi.clients.order import Order
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
        wallet: Wallet = None,
        base_url: str = None,
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
        self.wallet = wallet

        self.accounts = Accounts(base_url=base_url, api_key=api_key)
        self.app = App(base_url=base_url, api_key=api_key)
        self.order = Order(base_url=base_url, api_key=api_key)
        self.market = Market(base_url=base_url, api_key=api_key)

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
            **kwargs: Additional parameters for the order, such as price, limit_slippage, etc.

        Returns:
            A PostOrderResponse object containing the response from the API.

        Raises:
            ValueError: If the wallet is not initialized.
        """
        print(
            f"post_order: symbol={symbol}, side={side}, type={type}, quantity={quantity}, kwargs={kwargs}"
        )
        if not hasattr(self, "wallet") or self.wallet is None:
            raise ValueError("Wallet is not initialized")

        build_res = self.order.build_place_order_transaction(
            symbol, side, type, quantity, **kwargs
        )
        print(f"build_res: {build_res}")
        signed_tx = self.wallet.sign_tx(build_res["tx_hex"])
        submit_res = self.order.submit_place_order_transaction(
            build_res["order_id"], signed_tx, **kwargs
        )
        print(f"submit_res: {submit_res}")
        return submit_res
