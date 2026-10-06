import random

banca = random.randrange(17, 22)

jugadores = int(input("¿Cuántos jugadores van a jugar? "))

for jugador in range(1, jugadores + 1):
    print("Turno del jugador: ", jugador )

    puntos = 0
    continuar = True

    while continuar == True:
        carta = random.randrange(1, 6)
        puntos = puntos + carta
        print("Has sacado un ", carta, "Total: ", puntos)

        if puntos > 21:
            continuar = False
        else:
            print("¿Quieres otra carta?")
            print("1. Sí")
            print("2. No")
            opcion = int(input("Dime la opción: "))
            match opcion:
                case 1:
                    continuar = True
                case 2:
                    continuar = False

    print("Jugador: ", jugador, "Puntuación: ", puntos)
    if puntos > 21:
        print("Te has pasado de 21")
    elif puntos > banca:
        print("¡Ganas!")
    else:
        print("No has ganado a la banca.")