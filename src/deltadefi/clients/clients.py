# flake8: noqa: E501
from sidan_gin import HDWallet

from deltadefi.api_resources.auth import ApiHeaders
from deltadefi.clients.accounts import Accounts
from deltadefi.clients.markets import Markets
from deltadefi.clients.orders import Orders
from deltadefi.requests import PostOrderRequest
from deltadefi.responses import PostOrderResponse


class ApiClient:
    """
    ApiClient for interacting with the DeltaDeFi API.
    """

    def __init__(
        self,
        network: str = "preprod",
        jwt: str = None,
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
        self.base_url = base_url or "https://api-dev.deltadefi.io"
        headers: ApiHeaders = {
            "Content-Type": "application/json",
        }

        if network == "mainnet":
            self.network_id = 1
            base_url = "https://api-dev.deltadefi.io"  # TODO: input production link once available
        else:
            self.network_id = 0
            base_url = "https://api-dev.deltadefi.io"

        if jwt is not None:
            headers["Authorization"] = jwt

        if api_key is not None:
            headers["X-API-KEY"] = api_key

        if wallet is not None:
            self.wallet = wallet.signing_key

        self.accounts = Accounts(self)
        self.orders = Orders(self)
        self.markets = Markets(self)

    async def post_order(self, data: PostOrderRequest) -> PostOrderResponse:
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
