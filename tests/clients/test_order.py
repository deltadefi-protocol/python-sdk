# flake8: noqa
import os
import unittest

import dotenv

from deltadefi.clients import ApiClient
from deltadefi.responses import PostOrderResponse

dotenv.load_dotenv()


class TestOrder(unittest.TestCase):
    def setUp(self):
        api_key = os.getenv("DELTADEFI_API_KEY")
        password = os.getenv("TRADING_PASSWORD")
        if not api_key:
            self.skipTest("DELTADEFI_API_KEY not set in environment variables")
        if not password:
            self.skipTest("TRADING_PASSWORD not set in environment variables")
        api = ApiClient(api_key=api_key)
        api.load_operation_key(password)
        self.api = api

    def test_post_order(self):
        response: PostOrderResponse = self.api.post_order(
            symbol="ADAUSDM",
            side="sell",
            type="limit",
            quantity=51,
            price=15,
        )

        # Assert
        print(f"response: {response}")
        self.assertIn("order", response)


if __name__ == "__main__":
    unittest.main()
