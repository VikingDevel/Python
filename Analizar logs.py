import os

def analitzar_log(nom_fitxer):

    with open(nom_fitxer, "r", encoding="utf-8") as f:
        linies = f.readlines()

    # Eliminem salts de línia sobrants
    linies = [linia.strip() for linia in linies if linia.strip()]

    # Filtrem per paraula clau
    errors = [linia for linia in linies if "ERROR" in linia]
    warnings = [linia for linia in linies if "WARNING" in linia]

    num_errors = len(errors)
    num_warnings = len(warnings)

    # Les 5 línies amb ERROR més recents (assumint que el fitxer està
    # ordenat cronològicament, les últimes són les més recents)
    ultims_errors = errors[-5:]

    return num_errors, num_warnings, ultims_errors


def main():
    ruta = directorio_script = os.path.dirname(os.path.abspath(__file__))
    archivo = "log.txt"
    nom_fitxer = os.path.join(ruta, archivo)

    num_errors, num_warnings, ultims_errors = analitzar_log(nom_fitxer)

    print("--- RESUM DEL LOG ---")
    print(f"Total ERROR:   {num_errors}")
    print(f"Total WARNING: {num_warnings}")

    print("\n--- ÚLTIMES 5 LÍNIES AMB ERROR ---")
    if ultims_errors:
        for linia in ultims_errors:
            print(linia)
    else:
        print("No s'ha trobat cap línia amb ERROR.")

if __name__ == "__main__":
    main()
