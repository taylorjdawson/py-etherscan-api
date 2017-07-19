import pytest

from etherscan.contracts import Contract

# SNT Dutch Auction Contract Address
ADDRESS = '0x5ADCe2c8E78cA9102af302eAb5937F7CEFB0a266'
API_KEY = 'YourAPIkey'
SNT = 'snt'

def test_get_abi():
    contract = Contract(address=ADDRESS, api_key=API_KEY)
    abi = contract.get_abi()
    assert(SNT in abi)
