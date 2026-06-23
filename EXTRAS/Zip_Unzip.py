import zipfile
import os

def comprimir_archivos(lista_archivos, nombre_zip):
    """
    Comprime una lista de archivos en un archivo .zip.
    """
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

def descomprimir_archivo(nombre_zip, ruta_destino):
    """
    Descomprime un archivo .zip en la ruta especificada.
    """
    try:
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(ruta_destino)
            print(f"Archivo '{nombre_zip}' descomprimido en: {ruta_destino}")
    except Exception as e:
        print(f"Error al descomprimir: {e}")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Comprimir
    archivos_a_comprimir = ['documento.txt', 'imagen.png']
    comprimir_archivos(archivos_a_comprimir, 'archivo_comprimido.zip')

    # Descomprimir
    descomprimir_archivo('archivo_comprimido.zip', './carpeta_extraccion')