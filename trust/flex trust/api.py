"""Interface for Ethereum client and Trustery contract."""

import json
import os

#default ports or IPC file locations,
from web3.auto import w3
#Because of PoA
from web3.middleware import geth_poa_middleware

from userdata import getContract

import ipfshttpclient
#self.w3.geth.personal.unlock_account( self.w3.eth.defaultAccount,'1', 15000)
#from trustery.utils_py3 import encode_hex
# Initialise IPFS interface. 
CONTRACT_ABI = open("C://Users/pavlo/ethereum/flex_trust/contract/_contract_sol_Trustery.abi").read()

try:
    ipfsclient = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
except:
    ipfsclient = 0
if w3.isConnected():
    w3.eth.defaultAccount = w3.eth.accounts[0]
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    w3.geth.personal.unlock_account(w3.eth.defaultAccount, '1')
myContract = w3.eth.contract(address=getContract(), abi=CONTRACT_ABI)
#Because of PoA



def gethisconnected():
    if w3.isConnected():
        return True
    else: 
        return False

def ipfsisconnected():
    if ipfsclient == 0:
        return False
    else:
        return True
    #from trustery.testcontract import w3,myContract
    # Trustery contract constants.
    # TRUST_DEFAULT_ADDRESS = ''
    # TRUSTERY_ABI = json.load(open(os.path.join(os.path.dirname(trustery.__file__), 'trustery_abi.json')))

    # Ethereum client interface.

    

    #Need to unlock account for using
    

    #Create contract interface
    #myContract = w3.eth.contract(address=TRUSTERY_DEFAULT_ADDRESS, abi=TRUSTERY_ABI)


    #TODO need put into different file
    def encode_web3_hex(data):
        if data!=None:
            #Best solution i can find because toHex return 0x , need 0x0
            data = w3.toHex(data)
            data = '0x' + '0' * (66 - len(data)) + data[2:]
        else:
            data = None
        return data


    """
    previous decode
    def encode_api_data(data):
    
        Prepare arbitrary data to be send to the Ethereum client via the API.

        data: the data.
    
        if data is None:
            return None
        elif type(data) == str and data.startswith('0x'):
            # Return data if it is already hex-encoded.
            return data
        elif type(data) in [bool, int]:
            # Use native hex() to encode non-string data has encode_hex() does not support it.
            return hex(data)
        else:
            # Encode data using encode_hex(), the recommended way to encode Ethereum data.
            return '0x' + encode_hex(data)
    
        elif type(data) == long:
            # Use native hex() to encode long.
            encoded = hex(data)
            if encoded[-1:] == 'L':
                # Remove the trailing 'L' if found.
                encoded = encoded[:-1]
            return encoded
    """