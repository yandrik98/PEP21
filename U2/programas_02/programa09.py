"""
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
Programación en Python (PEP) - IES Leonardo Da Vinci - Álvaro García
U2P03-Programas_02. Estructuras repetitivas (bucles)
puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana.
"""

import random

banca = random.randrange(17, 22)
puntos = 0
continuar = True

while continuar:
    carta = random.randrange(1, 6)
    puntos = puntos + carta
    print("Has sacado un", carta, "Total:", puntos)

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

if puntos > 21:
    print("Te has pasado de 21")
elif puntos > banca:
    print("¡Ganas!")
else:
    print("No has ganado a la banca")