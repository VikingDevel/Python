import os

Users = "usuarios.txt"

def cargar_usuarios():
    """Carga los usuarios desde el archivo."""
    if not os.path.exists(Users):
        return []
    with open(Users, "r") as f:
        return [linia.strip() for linia in f.readlines()]

def guardar_usuarios(usuarios):
    """Guarda la lista de usuarios en el archivo."""
    with open(Users, "w") as f:
        for usuario in usuarios:
            f.write(usuario + "\n")

def listar_usuarios():
    usuarios = cargar_usuarios()
    print("\n--- Lista de usuarios ---")
    if not usuarios:
        print("La lista está vacía.")
    else:
        for idx, usuario in enumerate(usuarios, 1):
            print(f"{idx}. {usuario}")

def añadir_usuarios():
    nombre = input("Introduce el nombre del usuario: ").strip()
    if nombre:
        usuarios = cargar_usuarios()
        usuarios.append(nombre)
        guardar_usuarios(usuarios)
        print(f"Usuario '{nombre}' añadido correctamente.")

def eliminar_usuario():
    listar_usuarios()
    usuarios = cargar_usuarios()
    if not usuarios: return

    try:
        idx = int(input("\nNúmero de usuario a eliminar: ")) - 1
        if 0 <= idx < len(usuarios):
            eliminado = usuarios.pop(idx)
            guardar_usuarios(usuarios)
            print(f"Usuario '{eliminado}' eliminado.")
        else:
            print("Número no válido.")
    except ValueError:
        print("Entrada no válida.")

def menu():
    while True:
        print("\n--- GESTION DE USUARIOS ---")
        print("1. Listar usuarios")
        print("2. Añadir usuario")
        print("3. Eliminar usuario")
        print("4. SALIR")
        opcion = input("Selecciona una opción: ")

        if opcion == "1": listar_usuarios()
        elif opcion == "2": añadir_usuarios()
        elif opcion == "3": eliminar_usuario()
        elif opcion == "4": break
        else: print("Opción no válida.")

if __name__ == "__main__":
    menu()