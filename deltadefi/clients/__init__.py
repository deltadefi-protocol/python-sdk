from deltadefi.api_resources.wallet import DeFiWallet
from deltadefi.clients.accounts import Accounts
from deltadefi.clients.orders import Orders
from deltadefi.clients.markets import Markets
from deltadefi.api_resources.api_config import ApiConfig

class ApiClient:
    
    def __init__(self, config: ApiConfig, provided_base_url: str = None):
        if config.get('network') == 'mainnet': 
            self.network_id = 1
            self.base_url = 'https://api-dev.deltadefi.io'
        elif config.get('network') == 'preprod':
            self.base_url = 'https://api-dev.deltadefi.io'  # TODO: input production link once available
            self.network_id = 0 
        else:
            raise ConnectionRefusedError
        
        self.headers = {
            'Content-Type': 'application/json'
        }
        if config.get('jwt'):
            self.headers['Authorization'] = config['jwt']
        if config.get('apiKey'):
            self.headers['X-API-KEY'] = config['apiKey']
        if config.get('signingKey'): # TODO: import DefiWallet from mesh
            self.defiWallet = DeFiWallet(self)

        if provided_base_url:
            self.base_url = provided_base_url

        self.accounts = Accounts(self)
        self.orders = Orders(self)
        self.markets = Markets(self)