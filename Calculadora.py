while True:
    print ("CALCULADORA")
    print ("1 - Sumar")
    print ("2 - Restar")
    print ("3 - Multiplicar")
    print ("4 - Dividir")
    print ("5 - Salir de la calculadora")
    
    opcion = input("Elige una opción del menú (1-5): ")
    if opcion == "5": 
        print ("Gracias por haber usado esta calculadora!")
        break   
    if opcion not in ("1" , "2" , "3" , "4"):
            print ("Por favor, introduce la opción correcta")
    else:
        num1= float (input("Introduce el primer número: "))
        num2= float (input("Introduce el segundo número: "))
        if opcion == "1":
            print ("El resultado de la suma es igual a " , num1 + num2)
        elif opcion == "2":
            print ("El resultado de la resta es igual a " , num1 - num2)
        elif opcion == "3":
            print ("El resultado de la multiplicación es igual a " , num1 * num2)
        elif opcion == "4":
            if num2 == 0:
                print ("N0 se puede dividir por cero!")
            else:
                print ("El resultado de la división es igual a " , num1 /num2)
