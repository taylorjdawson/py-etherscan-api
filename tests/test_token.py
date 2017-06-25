import pytest

from etherscan.tokens import Tokens

DGD_TOKEN_SUPPLY = '1994946756800000'
DGD_TOKEN_BALANCE = '212900000000000'
AP_IKEY = 'YourAPIkey'
TOKEN_NAME = 'DGD'
ADDRESS = '0x4366ddc115d8cf213c564da36e64c8ebaa30cdbd'
API_KEY = 'YourAPIkey'
api = Tokens(tokenname=TOKEN_NAME, api_key=API_KEY)
def test_get_token_supply():
    assert (api.get_total_supply() == DGD_TOKEN_SUPPLY)

def test_get_token_balance():
    assert(api.get_token_balance(ADDRESS) == DGD_TOKEN_BALANCE)