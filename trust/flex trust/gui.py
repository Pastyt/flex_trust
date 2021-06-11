from tkinter import *
from tkinter.filedialog import askopenfilename

import api
import contract
import userdata
import managedb
import transactions
root = Tk()


def refreshAdress():
    contract.deploy_contract()

def genCA():
    d = {}
    d['C'] = 'US'
    d['ST'] = 'California'
    d['L'] = 'San Francisco '
    d['O'] = 'Wikimedia Foundation, Inc.'
    d['OU'] = 'IT'
    d['CN'] = '*.wikipedia.org'
    managedb.create_CA_cert(d)

def send_CRT():
    fname = askopenfilename(filetypes=(("Certificate", "*.crt"),
                                               ("All files", "*.*") ))
    
    transactions.send_cert(fname,'505')

def genCSR():
    managedb.create_CSR()

def signCSR():
    managedb.sing_CSR()

root.title('Flex Trust')
#root.geometry('500x400')
root.resizable(width=False, height=False)
lb_geth_text = Label(root, text="geth", fg="red")
lb_ipfs_text = Label(root, text="ipfs", fg="red")

btn_send_contract = Button(root,text="Send contract", command=refreshAdress)
btn_create_ca = Button(root,text="Generate CA cert", command=genCA)
btn_create_CSR = Button(root,text="Generate CSR cert", command=genCSR)
btn_sign_CSR = Button(root,text="Sign CSR cert", command=signCSR)
btn_send_CRT = Button(root,text="Send CRT to blockchain", command=send_CRT)

lb_geth_text.grid(column=1, row=3)
lb_ipfs_text.grid(column=2, row=3)


btn_send_contract.grid(column= 0,row=0)
btn_create_ca.grid(column=1, row = 0)
btn_create_CSR.grid(column=0, row = 1)
btn_sign_CSR.grid(column=1, row = 1)
btn_send_CRT.grid(column=2, row = 1)
if api.gethisconnected():
    lb_geth_text.config(fg="green")
if api.ipfsisconnected():
    lb_ipfs_text.config(fg="green")

root.mainloop()