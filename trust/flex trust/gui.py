from tkinter import *

import api

root = Tk()

def connect():
    myapi = api.myapi()
    if myapi.gethisconnected():
        geth_text.config(text="geth connected", fg="green")
    if myapi.ipfsisconnected():
        ipfs_text.config(text="ipfs connected", fg="green")

root.title('Flex Trust')
root.geometry('500x400')
root.resizable(width=False, height=False)

btn = Button(root, text="Connect", command=connect)
geth_text = Label(root, text="geth is not connected", fg="red")
ipfs_text = Label(root, text="ipfs is not connected", fg="red")

geth_text.grid(column=0, row=0)
ipfs_text.grid(column=1, row=0)
btn.grid(column=2, row=0)

root.mainloop()