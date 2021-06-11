from tkinter import *
from tkinter.filedialog import askopenfilename

import api
import contract
import userdata
import managedb
import transactions
import events
root = Tk()

def refreshAdress():
    contract.deploy_contract()

def show_Cert():
    events.showCert()

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

frame_main = LabelFrame(root,padx = 5, pady = 5, width= 300, height = 400)
frame_second = LabelFrame(root,padx = 5, pady = 5, width= 200, height = 400)
frame_down = LabelFrame(root,padx = 5, pady = 5, width= 300, height = 50)

lb_geth_text = Label(frame_down, text="geth", fg="red")
lb_ipfs_text = Label(frame_down, text="ipfs", fg="red")

btn_send_contract = Button(frame_second,text="Send contract", command=refreshAdress)
btn_create_ca = Button(frame_second,text="Generate CA cert", command=genCA)
btn_create_CSR = Button(frame_second,text="Generate CSR cert", command=genCSR)
btn_sign_CSR = Button(frame_second,text="Sign CSR cert", command=signCSR)
btn_send_CRT = Button(frame_second,text="Send CRT to blockchain", command=send_CRT)
btn_show_CRT = Button(frame_second,text="Show CRT in blockchain", command=show_Cert)

frame_main.grid(column= 0,row=0)
frame_second.grid(column= 1,row=0)
frame_down.grid(column= 1,row=1)



lb_geth_text.pack()
lb_ipfs_text.pack()


btn_send_contract.pack()
btn_create_ca.pack()
btn_show_CRT.pack()
btn_create_CSR.pack()
btn_sign_CSR.pack()
btn_send_CRT.pack()

if api.gethisconnected():
    lb_geth_text.config(fg="green")
if api.ipfsisconnected():
    lb_ipfs_text.config(fg="green")

root.mainloop()