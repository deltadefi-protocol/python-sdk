from deltadefi.clients import ApiClient
from deltadefi.responses import SignInResponse, BuildDepositTransactionResponse, SubmitDepositTransactionResponse, BuildWithdrawalTransactionResponse, SubmitWithdrawalTransactionResponse, GetOrderRecordResponse, GetDepositRecordsResponse, GetWithdrawalRecordsResponse, GetAccountBalanceResponse,GenerateNewAPIKeyResponse, GetTermsAndConditionResponse
from deltadefi.requests import SignInRequest, BuildDepositTransactionRequest, SubmitDepositTransactionRequest, BuildWithdrawalTransactionRequest, SubmitWithdrawalTransactionRequest
import requests

class Accounts:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def sign_in(self, data: SignInRequest) -> SignInResponse:
        auth_key = data['auth_key']
        wallet_address = data['wallet_address']
        headers = {
            'auth_key': auth_key,
            'Content-Type': 'application/json',
            'Authorization': self.api_client.headers['Authorization'],
            'X-API-KEY': self.api_client.headers['X-API-KEY'],
        }
        response = requests.post(
            f"{self.api_client.base_url}/accounts/signin",
            json={'wallet_address': wallet_address},
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    
    def getDepositRecords(self) -> GetDepositRecordsResponse:
        response = requests.get(
            f"{self.api_client.base_url}/accounts/deposit-records",
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()
    
    def getWithdrawalRecords(self) -> GetWithdrawalRecordsResponse:
        response = requests.get(
            f"{self.api_client.base_url}/accounts/withdrawal-records",
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()

    def getOrderRecords(self) -> GetOrderRecordResponse:
        response = requests.get(
            f"{self.api_client.base_url}/accounts/order-records",
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()

    def getAccountBalance(self) -> GetAccountBalanceResponse:
        response = requests.get(
            f"{self.api_client.base_url}/accounts/balance",
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()

    def createNewApiKey(self) -> GenerateNewAPIKeyResponse:
        response = requests.get(
            f"{self.api_client.base_url}/accounts/new-api-key",
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()

    def buildDepositTransaction(self, data: BuildDepositTransactionRequest) -> BuildDepositTransactionResponse:
        response = requests.post(
            f"{self.api_client.base_url}/accounts/deposit/build",
            json=data,
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()

    def buildWithdrawalTransaction(self, data: BuildWithdrawalTransactionRequest) -> BuildWithdrawalTransactionResponse:
        response = requests.post(
            f"{self.api_client.base_url}/accounts/withdrawal/build",
            json=data,
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()

    def submitDepositTransaction(self, data: SubmitDepositTransactionRequest) -> SubmitDepositTransactionResponse:
        response = requests.post(
            f"{self.api_client.base_url}/accounts/deposit/submit",
            json=data,
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()

    def submitWithdrawalTransaction(self, data: SubmitWithdrawalTransactionRequest) -> SubmitWithdrawalTransactionResponse:
        response = requests.post(
            f"{self.api_client.base_url}/accounts/withdrawal/submit",
            json=data,
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()
    
    def getTermsAndCondition(self) -> GetTermsAndConditionResponse:
        response = requests.get(
            f"{self.api_client.base_url}/accounts/terms-and-condition",
            headers=self.api_client.headers
        )
        response.raise_for_status()
        return response.json()