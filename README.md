# DeltaDeFi Python SDK

The DeltaDeFi Python SDK provides a convenient way to interact with the DeltaDeFi API. This SDK allows developers to easily integrate DeltaDeFi's features into their Python applications.

## Installation

To install the SDK, use `pip`:

```sh
pip install deltadefi-python-sdk
```

## Requirements

- Python 3.11 or higher

## Usage

### Initialization

To use the SDK, you need to initialize the ApiClient with your API configuration and wallet.

```python
from deltadefi.api_resources.api_config import ApiConfig
from deltadefi.clients.clients import ApiClient
from sidan_gin import HDWallet

# Initialize API configuration
network="mainnet",
api_key="your_api_key",

# Initialize HDWallet
wallet = HDWallet("your_wallet_mnemonic")

# Initialize ApiClient
api_client = ApiClient(network=network, api_key=api_key, wallet=wallet)
```

### Accounts

The Accounts client allows you to interact with account-related endpoints.

```python
from deltadefi.clients.accounts import Accounts

accounts_client = api_client.accounts

# Sign in
sign_in_request = SignInRequest(auth_key="your_auth_key", wallet_address="your_wallet_address")
sign_in_response = accounts_client.sign_in(sign_in_request)
print(sign_in_response)

# Get account balance
account_balance = accounts_client.get_account_balance()
print(account_balance)
```

### Markets

The Markets client allows you to interact with market-related endpoints.

```python
from deltadefi.clients.markets import Markets

markets_client = api_client.markets

# Get market depth
market_depth_request = GetMarketDepthRequest(pair="BTC/USD")
market_depth_response = markets_client.getDepth(market_depth_request)
print(market_depth_response)

# Get market price
market_price_request = GetMarketPriceRequest(pair="BTC/USD")
market_price_response = markets_client.getMarketPrice(market_price_request)
print(market_price_response)
```

### Orders

The Orders client allows you to interact with order-related endpoints.

```python
from deltadefi.clients.orders import Orders

orders_client = api_client.orders

# Build place order transaction
place_order_request = BuildPlaceOrderTransactionRequest(pair="BTC/USD", amount=1, price=50000)
place_order_response = orders_client.build_place_order_transaction(place_order_request)
print(place_order_response)

# Submit place order transaction
submit_order_request = SubmitPlaceOrderTransactionRequest(order_id="order_id")
submit_order_response = orders_client.submit_place_order_transaction(submit_order_request)
print(submit_order_response)
```

## License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

```
http://www.apache.org/licenses/LICENSE-2.0
```
