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
    