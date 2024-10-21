import subprocess
import tkinter as tk
from tkinter import scrolledtext
import paramiko
import socket

#####################################################################

# Se crea la funcion para abrir el socket SSH

def ssh_conn():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conexion = ssh.connect(host.get(), username=user.get(), password=passw.get(),port = port.get())
        arg ='cmd'
        subprocess.run(arg , shell=True)
        output.insert(tk.END, "Conectado\n")
    except Exception as e:
        output.insert(tk.END, f"Error de conexión. {str(e)}\n")

#------------------------------------------------------------------------------
# Creamos la interfaz gráfica.

root = tk.Tk( )
root.title ("Cliente SSH")
#root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Alumne_mati1\1-curspython\app\SSH\ssh.png"))

# Se crean las etiquetas .
tk.Label(root, text="Host:").grid(row=0, column=0)
tk.Label(root, text="Usuario:").grid(row=1, column=0)
tk.Label(root, text="Pass:").grid(row=2, column=0)
tk.Label(root, text="Puerto:").grid(row=3, column=0)

# Se crean los textbox donde introduciremos datos.
host = tk.Entry(root)
host.insert(0, "192.168.0.49")
host.grid(row=0, column=1)
user = tk.Entry(root)
user.insert(0, "")
user.grid(row=1, column=1)
passw = tk.Entry(root)
passw.insert(0, "")
passw.grid(row=2, column=1)
port = tk.Entry(root)
port.insert(0, "22") 
port.grid(row=3, column=1)


button = tk.Button(root, text="Connectar", command=ssh_conn)
button.grid(row=4, column=0, columnspan=1)


output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=10)
output.grid(row=10, column=0, columnspan=2)
root.mainloop()