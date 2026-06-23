import os
import shutil

ruta_carpeta = "%temp%"

for elemento in os.listdir(ruta_carpeta):
    ruta_elemento = os.path.join(ruta_carpeta, elemento)
    try:
        if os.path.isfile(ruta_elemento) or os.path.islink(ruta_elemento):
            os.unlink(ruta_elemento)  # Elimina el archivo
        elif os.path.isdir(ruta_elemento):
            shutil.rmtree(ruta_elemento)  # Elimina la subcarpeta y su contenido
    except Exception as e:
        print(f"Error al eliminar {ruta_elemento}: {e}")
