from api import w3
from api import ipfsclient
from api import myContract

def revoke_sign(signatureID):
     myContract.functions.revokeSignature(signatureID).transact()

def send_cert(path,identifier,):
    ipfs_data = ipfsclient.add(path)
    # {'Hash': 'QmWxS5aNTFEc9XbMX1ASvLET1zrqEaTssqt33rVZQCQb22', 'Name': 'test.txt'}
    ipfs_data = 'ipfs-block://' + ipfs_data['Hash']
    myContract.functions.addAttribute( 'CRT', False, 
        identifier.encode('utf-8'), ipfs_data , '' ).transact()
    # Add the attribute.
    