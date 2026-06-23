import os
import shutil

#Copiamos una carpeta de un directorio a otro.

ORpath = input("Introduce el directorio a copiar: ").strip()
DESTpath= input("Introduce el directorio de destino: ").strip()

try:
    shutil.copy(ORpath, DESTpath)
    print("Carpeta copiada.")
except FileExistsError:
    print("La carpeta destino ya existe.")
except Exception as e:
    print(f"Error al copiar: {e}")
    
