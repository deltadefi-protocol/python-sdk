# flake8: noqa
import os
import unittest

from sidan_gin import Wallet

from deltadefi.clients import ApiClient
from deltadefi.responses import PostOrderResponse


class TestOrder(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv("DELTADEFI_API_KEY")
        base_url = os.getenv("BASE_URL", "http://localhost:8080")
        mnemonic = os.getenv("SEED_PHRASE")
        print(f"Mnemonic: {mnemonic}")
        print(f"Mnemonic words: {len(mnemonic.split()) if mnemonic else 0}")
        wallet = Wallet.new_mnemonic(mnemonic)
        if not api_key:
            self.skipTest("DELTADEFI_API_KEY not set in environment variables")
        self.api = ApiClient(api_key=api_key, base_url=base_url, wallet=wallet)

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
