import configparser
import os

def getContract():
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        return config['CONTRACT']['address']
    except:
        return 'NULL'

def newContract(address):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['CONTRACT'] = {'address': address}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def getNewCertID():
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        a = config['CONTRACT']['certid']
    except:
        config['CONTRACT']['certid'] = 0
        a = config['CONTRACT']['certid']
    config['CONTRACT']['certid']+=1
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return a