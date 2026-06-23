import os

def comptar_fitxers_i_carpetes(ruta):

    num_fitxers = 0
    num_carpetes = 0

    with os.scandir(ruta) as elements:
        for element in elements:
            if element.is_file():
                num_fitxers += 1
            elif element.is_dir():
                num_carpetes += 1

    return num_fitxers, num_carpetes

def main():
    ruta = input("Introdueix la ruta del directori: ").strip()

    if not os.path.exists(ruta):
        print(f"Error: la ruta '{ruta}' no existeix.")
        return

    if not os.path.isdir(ruta):
        print(f"Error: '{ruta}' no és un directori.")
        return

    try:
        num_fitxers, num_carpetes = comptar_fitxers_i_carpetes(ruta)
        print(f"Hi ha {num_fitxers} fitxers i {num_carpetes} carpetes dins de '{ruta}'.")
    except PermissionError:
        print(f"Error: no tens permisos per accedir a '{ruta}'.")


if __name__ == "__main__":
    main()
