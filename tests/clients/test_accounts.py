# flake8: noqa
# get api_key from env
import os
import unittest

from deltadefi.clients import ApiClient
from deltadefi.responses import GetAccountBalanceResponse

api_key = os.getenv("DELTADEFI_API_KEY")


class TestAccounts(unittest.TestCase):

    def test_get_account_balance(self):
        if not api_key:
            self.skipTest("DELTADEFI_API_KEY not set in environment variables")

        # Arrange
        api = ApiClient(api_key=api_key)

        # Act
        response: GetAccountBalanceResponse = api.accounts.get_account_balance()
        print(f"response: {response}")

        # # Assert
        # print(f"response: {response}")
        # self.assertIn("token", response)
        # self.assertIn("is_first_time", response)


if __name__ == "__main__":
    unittest.main()
