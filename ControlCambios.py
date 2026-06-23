import os
import time
from datetime import datetime

# --- CONFIGURACIÓN ---
RUTA = "."  # Carpeta o archivo a controlar, por defecto la ruta de trabajo actual.
LOG = "cambios.log"
INTERVALO = 1

def registrar_evento(evento, path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = f"[{timestamp}] {evento}: {path}\n"
    print(mensaje.strip())
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(mensaje)

def obtener_estado(path):
    #Genera un diccionario con los archivos y su última fecha de modificación.
    estado = {}
    if os.path.isfile(path):
        estado[path] = os.path.getmtime(path)
    else:
        for raiz, _, archivos in os.walk(path):
            for archivo in archivos:
                path_completa = os.path.join(raiz, archivo)
                # se omite el fichero de log para evitar bucles de escritura
                if os.path.abspath(path_completa) != os.path.abspath(LOG):
                    estado[path_completa] = os.path.getmtime(path_completa)
    return estado

# --- BUCLE PRINCIPAL ---
if __name__ == "__main__":
    print(f"Vigilando: {os.path.abspath(RUTA)}")
    estado_anterior = obtener_estado(RUTA)

    try:
        while True:
            time.sleep(INTERVALO)
            estado_actual = obtener_estado(RUTA)

            # Detectar cambios y creaciones
            for path, mtime in estado_actual.items():
                if path not in estado_anterior:
                    registrar_evento("CREADO", path)
                elif mtime != estado_anterior[path]:
                    registrar_evento("MODIFICADO", path)

            # Detectar eliminaciones
            for path in estado_anterior:
                if path not in estado_actual:
                    registrar_evento("ELIMINADO", path)

            estado_anterior = estado_actual
    except KeyboardInterrupt:
        print("\nMonitorización finalizada.")