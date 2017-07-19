import pytest
from etherscan.stats import Stats

# TODO: These values are moving targets. Figure our a more reliable testing method

TOTAL_ETH_SUPPLY = "92765284717800000000000000"
API_KEY = 'YourAPIkey'

api = Stats(api_key=API_KEY)

def test_get_total_ether_supply():
    assert api.get_total_ether_supply() == TOTAL_ETH_SUPPLY

def test_get_ether_last_price():
    last_price = api.get_ether_last_price()
    assert type(last_price) is int