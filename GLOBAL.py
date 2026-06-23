import os
####################################################################################################
while True:
    print ("MIS PROGRAMAS")
    print ("1 - Calculadora")
    print ("2 - Número secreto")
    print ("3 - Analizador de LOGs")
    print ("4 - Generador de contraseñas")
    print ("5 - Piedra, papel o tijera")
    print ("6 - Contador de archivos")
    print ("7 - Listar archivos")
    print ("0 - SALIR")
####################################################################################################
    ruta = directorio_script = os.path.dirname(os.path.abspath(__file__))
    # Cargamos la ruta actual de trabajo en una variable, para poder llamar después al resto de ejecutables.

    opcion = input("Elige una opción del menú (1- a 7, 0 para salir.): ")
    if opcion == "0": 
        print ("Gracias por haber usado este programa!")
        break   
    if opcion not in ("1" , "2" , "3" , "4", "5" , "6" , "7"):
            print ("Por favor, introduce la opción correcta")
    else:
        if opcion == "1":
            print ("Has seleccionado la oción 1.")
            archivo = "Calculadora.py"
            path = os.path.join(ruta, archivo)
            with open(path) as f:
                codigo = f.read()
            exec(codigo)
        elif opcion == "2":
            print ("Has seleccionado la oción 2.")
            archivo = "Numero secreto.py"
            path = os.path.join(ruta, archivo)
            with open(path) as f:
                codigo = f.read()
            exec(codigo)
        elif opcion == "3":
            print ("Has seleccionado la oción 3.")
            archivo = "Analizar logs.py"
            path = os.path.join(ruta, archivo)
            with open(path) as f:
                codigo = f.read()
            exec(codigo)
        elif opcion == "4":
            print ("Has seleccionado la oción 4.")
            archivo = "Generador contraseñas.py"
            path = os.path.join(ruta, archivo)
            with open(path) as f:
                codigo = f.read()
            exec(codigo)
        elif opcion == "5":
            print ("Has seleccionado la oción 5.")
            archivo = "PPT.py"
            path = os.path.join(ruta, archivo)
            with open(path) as f:
                codigo = f.read()
            exec(codigo)
        elif opcion == "6":
            print ("Has seleccionado la oción 6.")
            archivo = "Contador archivos.py"
            path = os.path.join(ruta, archivo)
            with open(path) as f:
                codigo = f.read()
            exec(codigo)
        elif opcion == "7":
            print ("Has seleccionado la oción 7.")
            archivo = "Mostrar archivos.py"
            path = os.path.join(ruta, archivo)
            with open(path) as f:
                codigo = f.read()
            exec(codigo)


