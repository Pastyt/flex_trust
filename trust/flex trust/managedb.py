from OpenSSL import crypto
import os


CERT_FILE = "CA.crt"
KEY_FILE = "private.key"

def create_CA_cert(dict):

    # create a key pair
    k = crypto.PKey()
    
    k.generate_key(crypto.TYPE_RSA, 1024)

    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().C = dict['C']
    cert.get_subject().ST = dict['ST']
    cert.get_subject().L = dict['L']
    cert.get_subject().O = dict['O']
    cert.get_subject().OU = dict['OU']
    cert.get_subject().CN = dict['CN']
    cert.set_serial_number(0)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha256')

    open(CERT_FILE, "wb").write(
        crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    open(KEY_FILE, "wb").write(
        crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

def create_CSR():
    cert_req = crypto.X509Req()
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 1024)
    cert_req.get_subject().C = "Ru"
    cert_req.get_subject().ST = "State"
    cert_req.get_subject().L = "Location"
    cert_req.get_subject().O = "Organisation"
    #if models.RootCrt.objects.first().organizational_unit_name:
    cert_req.get_subject().OU = "Org unit name"
    cert_req.get_subject().CN = "www.CN.ru"
    #if models.RootCrt.objects.first().email:
    cert_req.get_subject().emailAddress = "email.ru"
    cert_req.set_pubkey(k)
    cert_req.sign(k, 'sha256')
    open("privateCSR.key", "wb").write(
        crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    open("req.csr", "wb").write(
        crypto.dump_certificate_request(crypto.FILETYPE_PEM, cert_req))

def sing_CSR():
    cert_req = crypto.load_certificate_request(crypto.FILETYPE_PEM, open("req.csr", "rb").read())
    cert_CA = crypto.load_certificate(crypto.FILETYPE_PEM, open(CERT_FILE, "rb").read())
    k = crypto.load_privatekey(crypto.FILETYPE_PEM, open(KEY_FILE, "rb").read())
    cert = crypto.X509()
    cert.set_serial_number(1)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert_CA.get_subject())
    cert.set_subject(cert_req.get_subject())
    cert.set_pubkey(cert_req.get_pubkey())
    cert.sign(k, 'sha256')
    open("newCert.crt", "wb").write(
        crypto.dump_certificate(crypto.FILETYPE_PEM, cert))