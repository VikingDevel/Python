import zipfile
import os
#################################################################################
def zip(lista_archivos, nombre_zip):
    ## Función comprimir
    try:
        with zipfile.ZipFile(nombre_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for archivo in lista_archivos:
                if os.path.exists(archivo):
                    # arcname evita que se guarde la ruta completa del sistema
                    zipf.write(archivo, os.path.basename(archivo))
                    print(f"Añadido: {archivo}")
                else:
                    print(f"Advertencia: {archivo} no encontrado.")
        print(f"\nArchivo '{nombre_zip}' creado exitosamente.")
    except Exception as e:
        print(f"Error al comprimir: {e}")

def unzip(nombre_zip, ruta_destino):
    ## Función descomprimir
    try:
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(ruta_destino)
            print(f"Archivo '{nombre_zip}' descomprimido en: {ruta_destino}")
    except Exception as e:
        print(f"Error al descomprimir: {e}")

# --- Ejemplo de uso ---
if __name__ == "__main__":

    archivos_a_comprimir = ['documento.txt', 'imagen.png']
    zip(archivos_a_comprimir, 'archivo_comprimido.zip')

    unzip('archivo_comprimido.zip', './carpeta_extraccion')