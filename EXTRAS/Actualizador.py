import os
import shutil
from datetime import datetime
import time
######################################################################
# Defincion de directorios para la simulación
ORIGEN = "./nuevos"
DESTINO = "./aplicacion"
BACKUP = "./bck"

def preparar_entorn():
    ## Crea las carpetas ficiticias para probar el script.
    
    os.makedirs(ORIGEN, exist_ok=True)
    os.makedirs(DESTINO, exist_ok=True)
    
    # Archivos actuales
    with open(os.path.join(DESTINO, "programa.exe"), "w") as f:
        f.write("old_ver_1.0")
    with open(os.path.join(DESTINO, "config.txt"), "w") as f:
        f.write("old_config_1.0")
        
    # Archivos de la actualización
    with open(os.path.join(ORIGEN, "programa.exe"), "w") as f:
        f.write("ver_2.0 (ACTUALITZADA)")
    with open(os.path.join(ORIGEN, "config.txt"), "w") as f:
        f.write("config_2.0")

def actualitzacion():
    print("=> Iniciando la simulacion de actualizacion en Python <=")
    time.sleep(1) # Se pone un pequeño delay para que parezca más realista

    # Paso 1 -  comprobación de los nuevos ficheros.
    print("[Paso 1 de 4] Comprobando si existen actualizaciones...")
    if not os.path.exists(ORIGEN) or not os.listdir(ORIGEN):
        print("ERROR: No hay actualizaciones disponibles.")
        return False
    print("-> Existe nueva versión del programa.")
    time.sleep(1)

    # Paso 1 -  Se hace copia de segjuridad
    print("[Paso 2 de 4] Realizando backup de los archivos actuales...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta_backup_actual = os.path.join(BACKUP, f"backup_{timestamp}")
    
    try:
        #Paso 2 - Copia todo el directorio a la carpeta de backup
        shutil.copytree(DESTINO, ruta_backup_actual)
        print(f"-> Backup realizado en : {ruta_backup_actual}")
    except Exception as e:
        print(f"ERROR: No se ha podido realizar el backup: {e}")
        return False
    time.sleep(1)

    # Paso 3 - Actualización de los ficheros
    print("[Paso 3 de 4] Actualizando el porgrama...")
    try:
        for ficheros in os.listdir(ORIGEN):
            origen_ficheros = os.path.join(ORIGEN, ficheros)
            destino_ficheros = os.path.join(DESTINO, ficheros)
            
            # Copia los archivos sobreescribiendo los existentes
            shutil.copy2(origen_ficheros, destino_ficheros)
            print(f"   Actualizado: {ficheros}")
            
        print("-> Actualización realizada correctamente.")
    except Exception as e:
        print(f"ERROR: No se ha podido realizar la actualizacion: {e}")
        return False
    time.sleep(1)

    # Paso 4 - Verificacion final.
    print("[Paso 4 de 4] Verificando la instalacion...")
    print("=> Actualizacion completada correctamente! <=")
    return True

# Se llaman a las funciones
if __name__ == "__main__":
    preparar_entorn()
    actualitzacion()
