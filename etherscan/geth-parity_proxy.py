from .client import Client

class GPProxy(Client):
    def __init__(self, address=Client.dao_address, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.module = self.URL_BASES['module'] + 'proxy'

    def get_block_number(self):
        pass
    def get_blokc_by_number(self):
        pass
