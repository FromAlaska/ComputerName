import os
import tkinter as tk
import socket
import getpass

root=tk.Tk()
root.title("Computer Name")

username = getpass.getuser()
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
textComputerInfo = "Username: {} \n Computer Name: {} \n IP Address: {}".format(username,hostname,ipaddress)

computerInfo = tk.Label(text=textComputerInfo,bg="SteelBlue3", fg="white", font=('helvetica', 12, 'bold'), height=4, width=50)
computerInfo.grid(row=0,column=1)
root.mainloop()