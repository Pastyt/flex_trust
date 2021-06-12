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

def show_Cert():
    logs = events.showCert()
    printdata = ''
    lb_data = Label(frame_main, text='', fg="black")
    lb_data.pack()

    for log in logs:
        #idk how to split this line :(
        printdata += str(log['certID'])+ " " + str(log['identifier']) + " " + str(int((int(log['expiry']) - time.time()) /(60 * 60 * 24))) + " " + str(log['expired']) + "\n"

    lb_data.config(text=printdata)
    
def genCA():
    e_c = Entry(frame_main, width = 50)
    e_st = Entry(frame_main, width = 50)
    e_l = Entry(frame_main, width = 50)
    e_o = Entry(frame_main, width = 50)
    e_ou = Entry(frame_main, width = 50)
    e_cn = Entry(frame_main, width = 50)

    e_c.insert(0, "Country (C)")
    e_st.insert(0, "State (S)")
    e_l.insert(0, "Locality (L)")
    e_o.insert(0, "Organization Name (O)")
    e_ou.insert(0, "Organizational Unit (OU)")
    e_cn.insert(0, "Common name (CN)")

    e_c.pack()
    e_st.pack()
    e_l.pack()
    e_o.pack()
    e_ou.pack()
    e_cn.pack()

    btn_input = Button(frame_main,text="Input", command=inputForGenCA)
    btn_input.pack()

def inputForGenCA(da):
    
    d = {}
    d['C'] = e_c.get()
    d['ST'] = e_st.get()
    d['L'] = e_l.get()
    d['O'] = e_o.get()
    d['OU'] = e_ou.get()
    d['CN'] = e_cn.get()
    print(d)
    managedb.create_CA_cert(d)

def send_CRT():
    fname = askopenfilename(filetypes=(("Certificate", "*.crt"),
                                               ("All files", "*.*") ))
    days = 500
    transactions.send_cert(fname,"Wikipedia",60 * 60 * 24 * days)

def genCSR():
    managedb.create_CSR()

def signCSR():
    managedb.sing_CSR()

def revokeCRT():
    transactions.revoke_sign(1)

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