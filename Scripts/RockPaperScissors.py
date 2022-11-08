#Piedra, Papel o Tijera.

import random, time

#Variables

global ronda
ronda = 0
global marcador_player
marcador_player = 0
global marcador_computer
marcador_computer = 0


def introduccion():
    print("     Bienvenido al juego de PIEDRA PAPEL O TIJERA")
    print("\n      Las Reglas son las siguientes.")
    print("\n1. La tijera gana al papel, pero esta es derrotada por la piedra")
    print("\n2. La piedra gana al la tijera, pero esta es ganada por el papel")
    print("\n3. El papel gana al la tijera, pero este es ganada por la tijera")

def reglas():
    global marcador_player
    global marcador_computer 
    global ronda
    ronda += 1

    lista = ['Tijeras','Papel','Piedra']
    computer = random.choice(lista)

    time.sleep(1)

    if player == 'tijeras' or 'Tijeras':
        if computer == 'Papel':
            print("Player WIN")
            marcador_player += 1
        elif computer == 'Piedra':
            print("Player LOSE")
            marcador_computer += 1
        elif computer == 'Tijeras':
            print("Player TIE")

    elif player == 'piedra' or 'Piedra':
        if computer == 'tijeras' or 'Tijeras':
            print("Player WIN")
            marcador_player += 1
        elif computer == 'Papel':
            print("Player LOSE")
            marcador_computer += 1
        elif computer == 'Piedra':
            print("Player TIE")
            
    elif player == 'papel' or 'Papel':
        if computer == 'Piedra':
            print("Player WIN")
            marcador_player += 1
        elif computer == 'Tijeras':
            print("Player LOSE")
            marcador_computer += 1
        elif computer == 'Papel':
            print("Player TIE")

    juego() 


def juego():
    global marcador_computer
    global marcador_player
    global player
    player = 0

    print("\n\nRonda Número %d" % ronda)
    print(f"\nMarcador {marcador_player} (Player) - {marcador_computer} (Computer)")

    print("¿Piedra, Papel o Tijeras?")

    player = input("\n([Q] para salir) | Elige: ")

    while player != "q" or "Q":
        reglas()
    else:
        finish()
        

def finish():
    print("\nGracias por jugar")
    print("\n \nSUS RESULTADO")

    print("\n\nHa jugado %d rondas" % ronda)
    print(f"\nMarcador {marcador_player} (Player) - {marcador_computer} (Computer)")

if __name__ == '__main__':
    introduccion()
    juego()
