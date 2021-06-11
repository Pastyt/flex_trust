#Need to see all cert + status
from api import myContract
from api import w3
from userdata import getBlock

def showCert():
    filterSended = myContract.events.SendedCertificate.createFilter(fromBlock=getBlock())
    filterRevoked = myContract.events.RevokedCertificate.createFilter(fromBlock=getBlock())

    getlogsSended = w3.eth.get_filter_logs(filterSended.filter_id)
    getlogsRevoked = w3.eth.get_filter_logs(filterRevoked.filter_id)

    logsSended = []
    logsRevoked = []
    for log in getlogsSended:
        logsSended.append(myContract.events.SendedCertificate().processLog(log))
    for log in getlogsRevoked:
        logsRevoked.append(myContract.events.RevokedCertificate().processLog(log))
    