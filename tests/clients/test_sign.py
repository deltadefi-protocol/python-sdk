# flake8: noqa
import unittest

from sidan_gin import Wallet


class TestSign(unittest.TestCase):

    def setUp(self):
        self.mnemonic = "summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer"
        self.root_key = "xprv1cqa46gk29plgkg98upclnjv5t425fcpl4rgf9mq2txdxuga7jfq5shk7np6l55nj00sl3m4syzna3uwgrwppdm0azgy9d8zahyf32s62klfyhe0ayyxkc7x92nv4s77fa0v25tufk9tnv7x6dgexe9kdz5gpeqgu"
        self.cli_key = (
            "51022b7e38be01d1cc581230e18030e6e1a3e949a1fdd2aeae5f5412154fe82b"
        )

    def test_sign_tx_mnemonic(self):
        self.wallet = Wallet.new_mnemonic(self.mnemonic)
        tx_hex = "84a4008182582004509185eb98edd8e2420c1ceea914d6a7a3142041039b2f12b4d4f03162d56f04018282581d605867c3b8e27840f556ac268b781578b14c5661fc63ee720dbeab663f1a000f42408258390004845038ee499ee8bc0afe56f688f27b2dd76f230d3698a9afcc1b66e0464447c1f51adaefe1ebfb0dd485a349a70479ced1d198cbdf7fe71a15d35396021a0002917d075820bdaa99eb158414dea0a91d6c727e2268574b23efe6e08ab3b841abe8059a030ca0f5d90103a0"
        signature = self.wallet.sign_tx(tx_hex)
        self.assertEqual(
            signature,
            "84a4008182582004509185eb98edd8e2420c1ceea914d6a7a3142041039b2f12b4d4f03162d56f04018282581d605867c3b8e27840f556ac268b781578b14c5661fc63ee720dbeab663f1a000f42408258390004845038ee499ee8bc0afe56f688f27b2dd76f230d3698a9afcc1b66e0464447c1f51adaefe1ebfb0dd485a349a70479ced1d198cbdf7fe71a15d35396021a0002917d075820bdaa99eb158414dea0a91d6c727e2268574b23efe6e08ab3b841abe8059a030ca1008182582089f4b576f05f5aad99bce0bdd51afe48529772f7561bb2ac9d84a4afbda1ecd658404cd1466fcc4579fa9c89656dbbd25ca659cccf2d2783417ef13a1b060bf836fbe8383c10e25c6fa323c1c81a0799e87e6cf3eaa25990113b27953a9836635a01f5d90103a0",
        )


if __name__ == "__main__":
    unittest.main()
