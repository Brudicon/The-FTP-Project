###################################################################
#   Function:
#       This program connects to a given host address (through SSH) 
#	given a username and password and lists all files in the current 
#	working directory.
#
#   Reason:
#       To learn a little more about file transfer protocol. 
#	I got the idea for this when I realized that I had to rely a 
#	lot on Putty and FileZilla for remote work on school computers.
#
#   Goal for this project:
#       To allow a user to input the address, username, 
#       and password manually and allow for direct user control 
#       of what commands are ushered to the host computer.
###################################################################


import paramiko
import tkinter as tk
from tkinter import *



def Connected(entries):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=entries[0].get(), username=entries[1].get(), password=entries[2].get())

    stdin, stdout, stderr = ssh.exec_command("ls")

    lines = 0
    curCol = 1
    outString = ''
    for c in stdout.readlines():
        outString = outString + c
        lines = lines + 1
        if lines == 10:
            PrintToGUI(outString, curCol)
            curCol = curCol + 1
            lines = 0
            outString = ''

    PrintToGUI(outString, curCol)
    lines = 0
    curCol = 1
    outString = ''



def PrintToGUI(output, col):
    label = tk.Label(root, text=output)
    label.grid(row = 4, column = col, sticky = tk.W, pady = 4)




def makeform(root):
    entries = []  
    tk.Label(root, text="Host name: ").grid(row = 0)
    tk.Label(root, text="Username: ").grid(row = 1)
    tk.Label(root, text="Password: ").grid(row = 2)
    e1 = tk.Entry(root)
    e2 = tk.Entry(root)
    e3 = tk.Entry(root)
    e1.insert(20, "")
    e2.insert(10, "")
    e3.insert(10, "")
    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)
    e3.grid(row = 2, column = 1)

    entries.append(e1)
    entries.append(e2)
    entries.append(e3)

    return entries


if __name__ == '__main__':
    root = tk.Tk()
    root.title('SSH')
    root.geometry('500x300')
    root.resizable(True, True)

    ents = makeform(root)
    root.bind('<Return>', (lambda event, e = ents: Connected(e)))
    b1 = tk.Button(root, text = 'Connect', command = (lambda e=ents: Connected(e))).grid(row = 3, column = 1, sticky = tk.W, pady = 4)

    res = tk.Label(root)

    root.mainloop()


