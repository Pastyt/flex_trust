from api import w3
from api import ipfsclient
from api import myContract
import time

def revoke_sign(crtID):
     myContract.functions.revokeCertificate(crtID).transact()

def send_cert(path,identifier,revoke):
    ipfs_data = ipfsclient.add(path)
    # {'Hash': 'QmWxS5aNTFEc9XbMX1ASvLET1zrqEaTssqt33rVZQCQb22', 'Name': 'test.txt'}
    ipfs_data = 'ipfs-block://' + ipfs_data['Hash']
    
    myContract.functions.sendCertificate(identifier.encode('utf-8'), ipfs_data , int(time.time() + revoke) ).transact()

    # Add the attribute.

#def test_send():

def revoke_test():
        w3.geth.personal.unlock_account(w3.eth.defaultAccount, '1')
        tx = myContract.functions.revokeCertificate(0).transact()
        w3.eth.waitForTransactionReceipt(tx)


def send_cert_test():
    w3.geth.personal.unlock_account(w3.eth.defaultAccount, '1')
    ipfs_data = ipfsclient.add('C:/Users/pavlo/ethereum/flex_trust/trust/flex trust/test.txt')
    ipfs_data = 'ipfs-block://' + ipfs_data['Hash']
    revoke = 555
    tx = myContract.functions.sendCertificate('Test'.encode('utf-8'), ipfs_data , int(time.time() + revoke) ).transact()
    w3.eth.waitForTransactionReceipt(tx)

def send_cert_test_pack():
    w3.geth.personal.unlock_account(w3.eth.defaultAccount, '1')
    ipfs_data = ipfsclient.add('C:/Users/pavlo/ethereum/flex_trust/trust/flex trust/test.txt')
    ipfs_data = 'ipfs-block://' + ipfs_data['Hash']
    revoke = 555
    tx = []
    
    for i in range(10):
        tx.append( myContract.functions.sendCertificate('Test'.encode('utf-8'), ipfs_data , int(time.time() + revoke) ).transact() )

    for i in range(10):
        w3.eth.waitForTransactionReceipt(tx[i])