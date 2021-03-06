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

def getBlock():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return int(config['BLOCK']['block'])

def rememberBlock(block):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['BLOCK'] = {'block': block}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def getNewCertID():
    config = configparser.ConfigParser()
    config.read('config.ini')
    a = config['CRT']['certid']
    config['CRT']['certid'] = str(int(config['CRT']['certid']) + 1)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return int(a)

def setCertIDtoZero():
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['CRT'] = {'certid': 1}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)