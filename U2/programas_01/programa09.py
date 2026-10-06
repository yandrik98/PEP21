"""
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
 La piedra gana a la tijera pero pierde contra el papel.
 El papel gana a la piedra pero pierde contra la tijera.
 La tijera gana al papel pero pierde contra la piedra.
"""





import random

print("1. Piedra")
print("2. Papel")
print("3. Tijera")

usuario = int(input("Seleccione una opción (1, 2 o 3): "))
aleatorio = random.randint(1, 3)

if usuario == 1:
    print("Tú: Piedra")
elif usuario == 2:
    print("Tú: Papel")
elif usuario == 3:
    print("Tú: Tijera")

if aleatorio == 1:
    print("Ordenador: Piedra")
elif aleatorio == 2:
    print("Ordenador: Papel")
else:
    print("Ordenador: Tijera")

if usuario == aleatorio:
    print("Empate.")
elif usuario == 1 and aleatorio == 3:
    print("¡Has ganado!")
elif usuario == 2 and aleatorio == 1:
    print("¡Has ganado!")
elif usuario == 3 and aleatorio == 2:
    print("¡Has ganado!")
else:
    print("Has perdido.")