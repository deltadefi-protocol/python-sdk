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

# Initialize ApiClient
api = ApiClient(network=network, api_key=api_key)
```

### Accounts

The Accounts client allows you to interact with account-related endpoints.

```python
# Get account balance
account_balance = api.accounts.get_account_balance()
print(account_balance)
```

### Markets

The Market client allows you to interact with market-related endpoints.

```python
# Get market depth
market_depth = api.markets.get_depth("ADAUSDM")
print(market_depth_response)

# Get market price
market_price_response = api.markets.get_market_price("ADAUSDM")
print(market_price_response)
```

### Orders

The Order client allows you to interact with order-related endpoints.

```python
api_key = os.environ.get("DELTADEFI_API_KEY")
password = os.environ.get("TRADING_PASSWORD")

api = ApiClient(api_key=api_key)
api.load_operation_key(password)

res = api.post_order(
    symbol="ADAUSDM",
    side="sell",
    type="limit",
    quantity=51,
    price=15,
)

print("Order submitted successfully.", res)
```

## Development

### Tests

Testing sdk:

```sh
DELTADEFI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx make test
```

## License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>
