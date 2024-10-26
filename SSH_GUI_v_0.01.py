import tkinter as tk
from tkinter import messagebox
import paramiko

###########################################################################################################
# Developed under GPL3 - Genrral Public License
# https://www.gnu.org/licenses/gpl-3.0.html

# This program is free software: 
# you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.


###########################################################################################################
# Se crea una clase que contiene el código de la ventana gráfica, el shell SSH y el input box desde el que le pasamos comandos a la máquina a la que nos conectamos


class SSHApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente SSH")

        tk.Label(root, text="Host").grid(row=0, column=0)
        tk.Label(root, text="User").grid(row=1, column=0)
        tk.Label(root, text="Pass").grid(row=2, column=0)

        self.host_entry = tk.Entry(root)
        self.username_entry = tk.Entry(root)
        self.password_entry = tk.Entry(root, show="*")

        self.host_entry.grid(row=0, column=1)
        self.username_entry.grid(row=1, column=1)
        self.password_entry.grid(row=2, column=1)

        tk.Button(root, text="Conectar", command=self.connect).grid(row=3, column=0, columnspan=2)

        self.command_entry = tk.Entry(root, width=50)
        self.command_entry.grid(row=4, column=0, padx=10, pady=10)

        tk.Button(root, text="Comando", command=self.execute_command, state=("disabled")).grid(row=4, column=1, padx=10, pady=10)

        self.output_text = tk.Text(root, height=50, width=100)
        self.output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def connect(self):
        self.host = self.host_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(self.host, username=self.username, password=self.password)
            messagebox.showinfo("Conexión", "Conexión correcta")
            
            # Si la conexión es correcta, se habilita el boton para enviar comandos a la máquina a la que nos hemos conectado.
            
            tk.Button(root, text="Comando", command=self.execute_command).grid(row=4, column=1, padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Conexión", f"Conexión fallida: {e}")

    def execute_command(self):
        command = self.command_entry.get()
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            output = stdout.read()
            error = stderr.read()
            self.output_text.delete(1.0, tk.END)  # Se limpia la pantalla cada vez que se ejecuta un nuevo comando
            self.output_text.insert(tk.END, f"Salida:\n{output}\n")
            if error:
                self.output_text.insert(tk.END, f"Error:\n{error}\n")
        except Exception as e:
            self.output_text.insert(tk.END, f"Error en la ejecución del comando: {e}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = SSHApp(root)
    root.mainloop()
