import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


from deltadefi import ApiClient

api = ApiClient(api_key="b13abb5bb86b96da341b59bc66612cc5")
account_balance = api.accounts.getAccountBalance()

print(account_balance)
