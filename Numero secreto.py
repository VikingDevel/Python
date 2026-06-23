import random
secret = random.randint(1, 20)
intentos = 0
print("=== Adivina el número!! ===")
print("He pensado un numero entre el 1 y el 20.")
while True:
    try:
        num = int(input("Indtoduce un número (Del 1 al 20): "))
        if num < 1 or num > 20:
            print("El número ha de estar entre el 1 y el 20.")
            continue
        intentos += 1
        if num < secret:
            print("Muy bajo!")
        elif num > secret:
            print("Muy alto!")
        else:
            print("Correcto!")
            print("Has necesitado", intentos, "intentos para adivinarlo.")
            break
    except ValueError:
        print("Por favor, introducde un n úmero entero.")
