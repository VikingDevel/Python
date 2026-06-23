import random

OPCIONS = ["pedra", "paper", "tisores"]

def triar_ordinador():

    return random.choice(OPCIONS)


def determinar_guanyador(usuari, ordinador):

    if usuari == ordinador:
        return "Empat!"

    # Combinacions on guanya l'usuari
    guanya_usuari = (
        (usuari == "pedra" and ordinador == "tisores") or
        (usuari == "paper" and ordinador == "pedra") or
        (usuari == "tisores" and ordinador == "paper")
    )

    if guanya_usuari:
        return "Has guanyat!"
    else:
        return "Ha guanyat l'ordinador!"


def demanar_eleccio():

    while True:
        eleccio = input("Tria pedra, paper o tisores (o escriu 'sortir'): ").lower().strip()

        if eleccio == "sortir":
            return eleccio

        if eleccio in OPCIONS:
            return eleccio

        print(f"Error: opció no vàlida. Has de triar entre {', '.join(OPCIONS)} o 'sortir'.")


def main():
    print("--- PEDRA, PAPER O TISORES ---")

    while True:
        eleccio_usuari = demanar_eleccio()

        if eleccio_usuari == "sortir":
            print("Gràcies per jugar! Adéu!")
            break

        eleccio_ordinador = triar_ordinador()
        print(f"L'ordinador ha triat: {eleccio_ordinador}")

        resultat = determinar_guanyador(eleccio_usuari, eleccio_ordinador)
        print(resultat)
        print("-" * 30)


if __name__ == "__main__":
    main()

