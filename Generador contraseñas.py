import random
import string

def generar_contrasenya(longitud):

    majuscules = string.ascii_uppercase
    minuscules = string.ascii_lowercase
    numeros = string.digits
    simbols = string.punctuation

    tots_caracters = majuscules + minuscules + numeros + simbols

    contrasenya = [
        random.choice(majuscules),
        random.choice(minuscules),
        random.choice(numeros),
        random.choice(simbols),
    ]

    for _ in range(longitud - len(contrasenya)):
        contrasenya.append(random.choice(tots_caracters))

    random.shuffle(contrasenya)

    return ''.join(contrasenya)

def demanar_longitud():
    while True:
        valor = input("Quina longitud vols per a la contrasenya? (mínim 4): ")
        if not valor.isdigit():
            print("Error: has d'introduir un número enter.")
            continue
        longitud = int(valor)
        if longitud < 4:
            print("Error: la longitud mínima ha de ser 4 per incloure tots els tipus de caràcter.")
            continue
        return longitud

def main():
    print("--- GENERADOR DE CONTRASENYES SEGURES ---")
    longitud = demanar_longitud()
    contrasenya = generar_contrasenya(longitud)
    print(f"\nLa teva contrasenya generada és:\n{contrasenya}")


if __name__ == "__main__":
    main()
