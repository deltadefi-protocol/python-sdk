import requests

from deltadefi.requests import (
    BuildDepositTransactionRequest,
    BuildWithdrawalTransactionRequest,
    SignInRequest,
    SubmitDepositTransactionRequest,
    SubmitWithdrawalTransactionRequest,
)
from deltadefi.responses import (
    BuildDepositTransactionResponse,
    BuildWithdrawalTransactionResponse,
    CreateNewAPIKeyResponse,
    GetAccountBalanceResponse,
    GetDepositRecordsResponse,
    GetOrderRecordResponse,
    GetTermsAndConditionResponse,
    GetWithdrawalRecordsResponse,
    SignInResponse,
    SubmitDepositTransactionResponse,
    SubmitWithdrawalTransactionResponse,
)


class Accounts:
    """
    Accounts client for interacting with the DeltaDeFi API.
    """

    def __init__(self, api_client):
        """
        Initialize the Accounts client.

        Args:
            api_client: An instance of the ApiClient.
        """
        self.api_client = api_client

    def sign_in(self, data: SignInRequest) -> SignInResponse:
        """
        Sign in to the DeltaDeFi API.

        Args:
            data: A SignInRequest object containing the authentication key and wallet address.

        Returns:
            A SignInResponse object containing the sign-in response.
        """
        auth_key = data["auth_key"]
        wallet_address = data["wallet_address"]
        headers = {
            "X-API-KEY": auth_key,
            "Content-Type": "application/json",
        }
        response = requests.post(
            f"{self.api_client.base_url}/accounts/signin",
            json={"wallet_address": wallet_address},
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def createNewApiKey(self) -> CreateNewAPIKeyResponse:
        """
        Create a new API key.

        Returns:
            A CreateNewAPIKeyResponse object containing the new API key.
        """
        response = requests.get(
            f"{self.api_client.base_url}/accounts/new-api-key",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def getDepositRecords(self) -> GetDepositRecordsResponse:
        """
        Get deposit records.

        Returns:
            A GetDepositRecordsResponse object containing the deposit records.
        """
        response = requests.get(
            f"{self.api_client.base_url}/accounts/deposit-records",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def getWithdrawalRecords(self) -> GetWithdrawalRecordsResponse:
        """
        Get withdrawal records.

        Returns:
            A GetWithdrawalRecordsResponse object containing the withdrawal records.
        """
        response = requests.get(
            f"{self.api_client.base_url}/accounts/withdrawal-records",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def getOrderRecords(self) -> GetOrderRecordResponse:
        """
        Get order records.

        Returns:
            A GetOrderRecordResponse object containing the order records.
        """
        response = requests.get(
            f"{self.api_client.base_url}/accounts/order-records",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def getAccountBalance(self) -> GetAccountBalanceResponse:
        """
        Get account balance.

        Returns:
            A GetAccountBalanceResponse object containing the account balance.
        """
        response = requests.get(
            f"{self.api_client.base_url}/accounts/balance",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def buildDepositTransaction(
        self, data: BuildDepositTransactionRequest
    ) -> BuildDepositTransactionResponse:
        """
        Build a deposit transaction.

        Args:
            data: A BuildDepositTransactionRequest object containing the deposit transaction details.

        Returns:
            A BuildDepositTransactionResponse object containing the built deposit transaction.
        """
        response = requests.post(
            f"{self.api_client.base_url}/accounts/deposit/build",
            json=data,
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def buildWithdrawalTransaction(
        self, data: BuildWithdrawalTransactionRequest
    ) -> BuildWithdrawalTransactionResponse:
        """
        Build a withdrawal transaction.

        Args:
            data: A BuildWithdrawalTransactionRequest object containing the withdrawal transaction details.

        Returns:
            A BuildWithdrawalTransactionResponse object containing the built withdrawal transaction.
        """
        response = requests.post(
            f"{self.api_client.base_url}/accounts/withdrawal/build",
            json=data,
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def submitDepositTransaction(
        self, data: SubmitDepositTransactionRequest
    ) -> SubmitDepositTransactionResponse:
        """
        Submit a deposit transaction.

        Args:
            data: A SubmitDepositTransactionRequest object containing the deposit transaction details.

        Returns:
            A SubmitDepositTransactionResponse object containing the submitted deposit transaction.
        """
        response = requests.post(
            f"{self.api_client.base_url}/accounts/deposit/submit",
            json=data,
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def submitWithdrawalTransaction(
        self, data: SubmitWithdrawalTransactionRequest
    ) -> SubmitWithdrawalTransactionResponse:
        """
        Submit a withdrawal transaction.

        Args:
            data: A SubmitWithdrawalTransactionRequest object containing the withdrawal transaction details.

        Returns:
            A SubmitWithdrawalTransactionResponse object containing the submitted withdrawal transaction.
        """
        response = requests.post(
            f"{self.api_client.base_url}/accounts/withdrawal/submit",
            json=data,
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()

    def getTermsAndCondition(self) -> GetTermsAndConditionResponse:
        """
        Get terms and conditions.

        Returns:
            A GetTermsAndConditionResponse object containing the terms and conditions.
        """
        response = requests.get(
            f"{self.api_client.base_url}/accounts/terms-and-condition",
            headers=self.api_client.headers,
        )
        response.raise_for_status()
        return response.json()
