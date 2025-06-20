# DeltaDeFi Python SDK

The DeltaDeFi Python SDK provides a convenient way to interact with the DeltaDeFi API. This SDK allows developers to easily integrate DeltaDeFi's features into their Python applications.

## Installation

To install the SDK, use `pip`:

```sh
pip install deltadefi
```

## Requirements

- Python 3.11 or higher

## Usage

### Initialization

To use the SDK, you need to initialize the ApiClient with your API configuration and wallet.

```python
from deltadefi.clients import ApiClient
from sidan_gin import HDWallet

# Initialize API configuration
network="preprod",
api_key="your_api_key",

# Initialize HDWallet
wallet = HDWallet("your_wallet_mnemonic")

# Initialize ApiClient
api = ApiClient(network=network, api_key=api_key, wallet=wallet)
```

### Accounts

The Accounts client allows you to interact with account-related endpoints.

```python
# Get account balance
account_balance = api.accounts.get_account_balance()
print(account_balance)
```

### Market

The Market client allows you to interact with market-related endpoints.

```python
# Get market depth
market_depth = api.market.get_depth("ADAUSDM")
print(market_depth_response)

# Get market price
market_price_response = api.market.get_market_price("ADAUSDM")
print(market_price_response)
```

### Order

The Order client allows you to interact with order-related endpoints.

```python
# Build place order transaction
place_order_request = BuildPlaceOrderTransactionRequest(pair="BTC/USD", amount=1, price=50000)
place_order_response = api.order.build_place_order_transaction(symbol="ADAUSDM", amount=50, price=0.75, type="limit")
print(place_order_response)

# Submit place order transaction
submit_order_response = api.order.submit_place_order_transaction(signed_tx="<signed_tx>", order_id="<order_id>")
print(submit_order_response)
```

## Development

### Tests

Testing sdk:

```sh
DELTADEFI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx make test
```

## License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>
