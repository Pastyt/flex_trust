from api import w3
from solc import compile_standard
import json

from userdata import newContract
from api import CONTRACT_ABI
from api import myContract
def deploy_contract():
    #Need to compile before start
    #TODO Change to os.path
    bytecode =  open("C://Users/pavlo/ethereum/flex_trust/contract/_contract_sol_Trustery.bin")
    MyContract = w3.eth.contract(abi=CONTRACT_ABI, bytecode=bytecode.read())
    

    tx_hash = MyContract.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    newContract(tx_receipt.contractAddress)
    myContract = w3.eth.contract( address=tx_receipt.contractAddress, abi=CONTRACT_ABI)
