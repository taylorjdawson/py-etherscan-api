import pytest
from etherscan.accounts import Account



ADDRESS = '0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b'
ADDRESSES = [ADDRESS, '0x63a9975ba31b0b9626b34300f7f627147df1f526', '0x198ef1ec325a96cc354c7266a038be8b5c558f67']

# Theses balances are bound to change; just a reminder
BALANCES = ["18550740724073055320", "332567136222827062478", "10846199677572223951724"]
ACT_BALANCE = '18550740724073055320'

API_KEY = 'YourAPIkey'

PAGE = 1
OFFSET = 1
SORT_ASC = 'asc'
EXTERNAL = False
INTERNAL = True

account = Account(ADDRESS, API_KEY)
accounts = Account(ADDRESSES, API_KEY)

def test_get_balance():
    assert account.get_balance() == ACT_BALANCE

def test_get_balance_multiple():
    balances = [b['balance'] for b in accounts.get_balance_multiple()]
    assert balances == BALANCES

# def test_get_internal_transaction_page():
#     assert account.get_transaction_page(PAGE, OFFSET, SORT_ASC, INTERNAL) ==
#
# def test_get_external_transaction_page():
#     assert account.get_transaction_page(PAGE, OFFSET, SORT_ASC, EXTERNAL) ==
#
# def test_get_all_transactions():
#
# def test_get_blocks_mined_page():
#
# def test_get_all_blocks_mined():
#
# def test_get_internal_by_hash():
#
# def test_update_transactions():
