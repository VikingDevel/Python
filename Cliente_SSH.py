import os
import tkinter
import paramiko


#####################################################################

ssh = paramiko.SSHClient()
# Se crea la funcion para abrir el socket SSH

def ssh_connect(host):
    