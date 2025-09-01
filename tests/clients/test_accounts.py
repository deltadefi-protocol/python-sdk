# flake8: noqa
import os
import unittest

from deltadefi.clients import ApiClient
from deltadefi.responses import GetAccountBalanceResponse
from deltadefi.responses.accounts import GetOperationKeyResponse


class TestAccounts(unittest.TestCase):
    def setUp(self):
        api_key = os.getenv("DELTADEFI_API_KEY")
        base_url = os.getenv("BASE_URL", "http://localhost:8080")
        print(api_key)
        if not api_key:
            self.skipTest("DELTADEFI_API_KEY not set in environment variables")
        self.api = ApiClient(api_key=api_key, base_url=base_url)

    def test_get_operation_key(self):
        response: GetOperationKeyResponse = self.api.accounts.get_operation_key()

        # Assert
        print(f"response: {response}")
        self.assertIn("encrypted_operation_key", response)
        self.assertIn("operation_key_hash", response)

    def test_get_account_balance(self):
        response: GetAccountBalanceResponse = self.api.accounts.get_account_balance()
        print(f"response: {response}")

    def test_get_order_records(self):
        response: GetAccountBalanceResponse = self.api.accounts.get_order_records(
            "openOrder"
        )
        print(f"response: {response}")

    # # Assert
    # print(f"response: {response}")
    # self.assertIn("token", response)
    # self.assertIn("is_first_time", response)


if __name__ == "__main__":
    unittest.main()
