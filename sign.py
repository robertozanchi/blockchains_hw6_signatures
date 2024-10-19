import eth_account
from web3 import Web3
from eth_account.messages import encode_defunct


def sign(m):
    w3 = Web3()
    # create an eth account and recover the address (derived from the public key) and private key
    # your code here

    eth_address = None  # Eth account
    private_key = None

    # generate signature
    # your code here

    signed_message = None

    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)

    return eth_address, signed_message
