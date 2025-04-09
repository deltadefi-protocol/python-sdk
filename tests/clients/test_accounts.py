# flake8: noqa
import unittest

from deltadefi.clients.accounts import Accounts
from deltadefi.clients.clients import ApiClient
from deltadefi.requests import SignInRequest
from deltadefi.responses import SignInResponse


class TestAccounts(unittest.TestCase):

    def test_sign_in(self):
        # Arrange
        api = ApiClient()
        sign_in_data: SignInRequest = {
            "wallet_address": "addr_test1qqzgg5pcaeyea69uptl9da5g7fajm4m0yvxndx9f4lxpkehqgezy0s04rtdwlc0tlvxafpdrfxnsg7ww68ge3j7l0lnszsw2wt",
            "auth_key": "test",
        }

        # Act
        response: SignInResponse = api.accounts.sign_in(sign_in_data)
        print(f"response: {response}")

        # Assert
        print(f"response: {response}")
        self.assertIn("token", response)
        self.assertIn("is_first_time", response)


if __name__ == "__main__":
    unittest.main()
