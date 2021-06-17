#Need to see all cert + status
from api import myContract
from api import w3
from userdata import getBlock
import time

def showCert():
    t1 = open('C:/Users/pavlo/ethereum/show_only_geth.txt', 'a')

    filterSended = myContract.events.SendedCertificate.createFilter(fromBlock=getBlock())
    filterRevoked = myContract.events.RevokedCertificate.createFilter(fromBlock=getBlock())

    start = time.time()
    getlogsSended = w3.eth.get_filter_logs(filterSended.filter_id)
    getlogsRevoked = w3.eth.get_filter_logs(filterRevoked.filter_id)
    start =str(time.time()-start)
    t1.write(start + '\n')

    logsSended = []
    logsRevoked = []
    for log in getlogsSended:
        logsSended.append(myContract.events.SendedCertificate().processLog(log))
    for log in getlogsRevoked:
        logsRevoked.append(myContract.events.RevokedCertificate().processLog(log))
    

    return sortInfo(logsSended,logsRevoked)


def sortInfo(logsSended,logsRevoked):
    logsfinal = []

    for i in range(len(logsSended)):
        log = {}
        log['certID'] = logsSended[i]['args']['certID']
        log['identifier'] = bytes(logsSended[i]['args']['identifier']).decode('utf-8').replace('\x00', '')
        log['data'] = logsSended[i]['args']['data']
        log['expiry'] = logsSended[i]['args']['expiry']
        if time.time() > logsSended[i]['args']['expiry']:
            log['expired'] = True
            logsfinal.append(log)
            continue
        log['expired'] = False

        for j in range(len(logsRevoked)):
            if log['certID'] == logsRevoked[j]['args']['certID']:
                log['expired'] = True

        logsfinal.append(log)

    return logsfinal