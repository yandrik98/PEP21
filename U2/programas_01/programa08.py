"""
Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
Puedes pedir el valor de cada tirada de dados por teclado o usar la la función
random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
debes poner import random al inicio del programa)
"""



import random

a1 = random.randrange(1, 7)
a2 = random.randrange(1, 7)
b1 = random.randrange(1, 7)
b2 = random.randrange(1, 7)

total1 = a1 + a2
total2 = b1 + b2
max1 = max(a1, a2)
max2 = max(b1, b2)

print(f"Jugador 1: {a1} y {a2} (total {total1})")
print(f"Jugador 2: {b1} y {b2} (total {total2})")

if total1 > total2:
    print("Gana el jugador 1.")
elif total2 > total1:
    print("Gana el jugador 2.")
elif max1 > max2:
    print("Mismo total. Gana el jugador 1 por el dado más alto.")
elif max2 > max1:
    print("Mismo total. Gana el jugador 2 por el dado más alto.")
else:
    print("Empate.")