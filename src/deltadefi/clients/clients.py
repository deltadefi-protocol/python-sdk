# flake8: noqa: E501
from sidan_gin import HDWallet

from deltadefi.clients.accounts import Accounts
from deltadefi.clients.app import App
from deltadefi.clients.market import Market
from deltadefi.clients.order import Order
from deltadefi.responses import PostOrderResponse


class ApiClient:
    """
    ApiClient for interacting with the DeltaDeFi API.
    """

    def __init__(
        self,
        network: str = "preprod",
        api_key: str = None,
        wallet: HDWallet = None,
        base_url: str = None,
    ):
        """
        Initialize the ApiClient.

        Args:
            config: An instance of ApiConfig containing the API configuration.
            wallet: An instance of HDWallet for signing transactions.
            base_url: Optional; The base URL for the API. Defaults to "https://api-dev.deltadefi.io".
        """
        if network == "mainnet":
            self.network_id = 1
            self.base_url = "https://api-dev.deltadefi.io"  # TODO: input production link once available
        else:
            self.network_id = 0
            self.base_url = "https://api-dev.deltadefi.io"

        if base_url:
            self.base_url = base_url

        self.api_key = api_key
        self.wallet = wallet

        self.accounts = Accounts(base_url=base_url, api_key=api_key)
        self.app = App(base_url=base_url, api_key=api_key)
        self.order = Order(base_url=base_url, api_key=api_key)
        self.market = Market(base_url=base_url, api_key=api_key)

    async def post_order(self, **kwargs) -> PostOrderResponse:
        """
        Post an order to the DeltaDeFi API.

        Args:
            data: A PostOrderRequest object containing the order details.

        Returns:
            A PostOrderResponse object containing the response from the API.

        Raises:
            ValueError: If the wallet is not initialized.
        """
        if not hasattr(self, "wallet") or self.wallet is None:
            raise ValueError("Wallet is not initialized")

        build_res = ""  # TODO: import wallet build order
        signed_tx = self.wallet.sign_tx(build_res["tx_hex"])
        submit_res = signed_tx + ""  # TODO: import wallet submit tx
        return submit_res
