num = int(input ("Introduce el numero del que quieras saber la tabla de multiplicar: "))
multiplicador = int (input ("Hasta que numero quieres los resultados?: "))
total = 0
while total <= multiplicador:
    print (" El resultado de multiplicar" ,num , "por",total, "es igual a" ,num*total)
    total +=1
