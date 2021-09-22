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


ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='', username='', password='')

stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.readlines())

