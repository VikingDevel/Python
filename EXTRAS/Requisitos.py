import shutil
import sys

def verificar_espacio_disco(ruta_inst, requisitos_espacio):

    # Obtenim les estadístiques del disc
    total, usado, libre = shutil.disk_usage(ruta_inst)
    
    # Convertim el bytes a Gigabytes (1 GB = 1024^3 bytes)
    libre_gb = libre / (2**30)
    
    print(f"Espacio libre disponible: {libre_gb:.2f} GB")
    print(f"Espacio necesario: {requisitos_espacio} GB")
    
    return libre_gb >= requisitos_espacio


ruta = "C:\\Program Files"  # Se añade la ruta donde queremos instalar el programa
espacio_necesario = 5.0 

if verificar_espacio_disco(ruta, espacio_necesario):
    print("✅ Hay espacio suficiente. Procediendo con la instalación")
else:
    print("❌ Error: No hay suficiente espacio. Se cancela la instalación.")
    sys.exit(1) 