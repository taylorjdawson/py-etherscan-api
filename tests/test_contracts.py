import pytest

from etherscan.contracts import Contract

# SNT Dutch Auction Contract
ADDRESS = '0x5ADCe2c8E78cA9102af302eAb5937F7CEFB0a266'
SNT = 'snt'
API_KEY = 'YourAPIkey'

def test_get_abi():
    contract = Contract(address=ADDRESS, api_key=API_KEY)
    abi = contract.get_abi()
    assert(SNT in abi)
