import os

def llistar_fitxers_i_carpetes(ruta):

    elements_llistats = []

    with os.scandir(ruta) as elements:
        for element in elements:
            if element.is_file():
                tipus = "Fitxer"
            elif element.is_dir():
                tipus = "Carpeta"
            else:
                tipus = "Altre"
            elements_llistats.append((element.name, tipus))

    return elements_llistats


def main():
    ruta = input("Introdueix la ruta del directori: ").strip()

    if not os.path.exists(ruta):
        print(f"Error: la ruta '{ruta}' no existeix.")
        return

    if not os.path.isdir(ruta):
        print(f"Error: '{ruta}' no és un directori.")
        return

    try:
        elements_llistats = llistar_fitxers_i_carpetes(ruta)
    except PermissionError:
        print(f"Error: no tens permisos per accedir a '{ruta}'.")
        return

    if not elements_llistats:
        print(f"El directori '{ruta}' està buit.")
        return

    print(f"\nContingut de '{ruta}':")
    for nom, tipus in elements_llistats:
        print(f"  [{tipus}] {nom}")


if __name__ == "__main__":
    main()
