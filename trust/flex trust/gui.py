from tkinter import *
from tkinter.filedialog import askopenfilename
import time

import api
import contract
import userdata
import managedb
import transactions
import events

root = Tk()

def refreshAdress():
    contract.deploy_contract()
    lb_mainframe_text.config(text="Contract sended")
    lb_mainframe_text.pack()


def show_Cert():
    logs = events.showCert()
    printdata = ''

    for log in logs:
        #idk how to split this line :(
        printdata += str(log['certID'])+ " " + str(log['identifier']) + " " + str(int((int(log['expiry']) - time.time()) /(60 * 60 * 24))) + " " + str(log['expired']) + "\n"
    if len(printdata) == 0:
        printdata = "Contract is empty"
    lb_mainframe_text.config(text=printdata)
    lb_mainframe_text.pack()
    
def genCA(mode):
    global e_c, e_st, e_l, e_o, e_ou, e_cn, btn_input
    lb_mainframe_text.pack_forget()

    e_c= Entry(frame_main, width = 50)
    e_st= Entry(frame_main, width = 50)
    e_l= Entry(frame_main, width = 50)
    e_o= Entry(frame_main, width = 50)
    e_ou= Entry(frame_main, width = 50)
    e_cn= Entry(frame_main, width = 50)

    e_c.insert(0, "Country (C)")
    e_st.insert(0, "State (S)")
    e_l.insert(0, "Locality (L)")
    e_o.insert(0, "Organization Name (O)")
    e_ou.insert(0, "Organizational Unit (OU)")
    e_cn.insert(0, "Common name (CN)")

    for e in (e_c,e_st,e_l,e_o,e_ou,e_cn):
        e.pack()
    
    btn_input = Button(frame_main,text="Input", command=lambda: inputForGenCA(mode))
    btn_input.pack()

def inputForGenCA(mode):
    
    d = {}
    d['C'] = e_c.get()
    d['ST'] = e_st.get()
    d['L'] = e_l.get()
    d['O'] = e_o.get()
    d['OU'] = e_ou.get()
    d['CN'] = e_cn.get()
    
    if mode == 0:
        managedb.create_CA_cert(d)
    else:
        managedb.create_CSR(d)

    for e in (e_c,e_st,e_l,e_o,e_ou,e_cn,btn_input):
        e.destroy()
    
    if mode == 0:
        lb_mainframe_text.config(text="Certificate created and sended to blockchain succesfully")
    else:
        lb_mainframe_text.config(text="CSR created succesfully")
    lb_mainframe_text.pack()

def send_CRT():
    fname = askopenfilename(filetypes=(("Certificate", "*.crt"),
                                               ("All files", "*.*") ))
    days = 500
    transactions.send_cert(fname,"Wikipedia",60 * 60 * 24 * days)

def genCSR():

    managedb.create_CSR()

def signCSR():
    fname = askopenfilename(filetypes=(("Certificate signing request", "*.csr"),
                                               ("All files", "*.*") ))
    global e_expiry, btn_expiry
    e_expiry= Entry(frame_main, width = 50)
    e_expiry.insert(0, "Expiry time (in days)")
    e_expiry.pack()
    btn_expiry = Button(frame_main,text="Send", command=lambda: sendCRS(fname))
    btn_expiry.pack()
    

def sendCRS(fname):
    expiry = int(e_expiry.get())
    e_expiry.destroy()
    btn_expiry.destroy()

    managedb.sing_CSR(fname,60 * 60 * 24 *expiry)
    lb_mainframe_text.config(text="CSR signed and sended to blockchain")
    lb_mainframe_text.pack()


def revokeCRT():
    lb_mainframe_text.pack_forget()
    global e_revoke, btn_revoke
    e_revoke= Entry(frame_main, width = 50)
    e_revoke.insert(0, "ID of revoked cert?")
    e_revoke.pack()
    btn_revoke = Button(frame_main,text="Revoke", command=sendRevoke)
    btn_revoke.pack()
    

def sendRevoke():
    revoke = int(e_revoke.get())
    e_revoke.destroy()
    btn_revoke.destroy()
    lb_mainframe_text.config(text="Certificate revoked")
    lb_mainframe_text.pack()
    transactions.revoke_sign(revoke)


root.title('Flex Trust')
#root.geometry('500x400')
root.resizable(width=False, height=False)


frame_main = LabelFrame(root,padx = 5, pady = 5, width= 300, height = 400)
frame_second = LabelFrame(root,padx = 5, pady = 5, width= 200, height = 400)
frame_down = LabelFrame(root,padx = 5, pady = 5, width= 300, height = 50)

lb_mainframe_text = Label(frame_main)
lb_geth_text = Label(frame_down, text="geth", fg="red")
lb_ipfs_text = Label(frame_down, text="ipfs", fg="red")

btn_send_contract = Button(frame_second,text="Send contract", command=refreshAdress)
btn_create_ca = Button(frame_second,text="Generate CA cert", command=lambda: genCA(0))
btn_create_CSR = Button(frame_second,text="Generate CSR", command=lambda: genCA(1))
btn_sign_CSR = Button(frame_second,text="Sign CSR cert", command=signCSR)
btn_send_CRT = Button(frame_second,text="Send CRT to blockchain", command=send_CRT)
btn_show_CRT = Button(frame_second,text="Show CRT in blockchain", command=show_Cert)
btn_revoke_CRT = Button(frame_second,text="Revoke CRT", command=revokeCRT)


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
btn_revoke_CRT.pack()
if api.gethisconnected():
    lb_geth_text.config(fg="green")
if api.ipfsisconnected():
    lb_ipfs_text.config(fg="green")

root.mainloop()