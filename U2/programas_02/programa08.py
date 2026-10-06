"""
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).
Mejora el programa de forma que el usuario tenga solo 3 intentos.

"""
import random

numAleatorio = random.randrange(1, 21)
intentos = 0
acertado = False

while intentos < 3 and acertado == False:
    num = int(input("Adivina el número: "))
    intentos = intentos + 1

    if num == numAleatorio:
        acertado = True
    elif numAleatorio > num:
        print("El número es mayor.")
    else:
        print("El número menor.")

if acertado:
    print("¡Has acertado en", intentos, "intentos!")
else:
    print("Has agotado los 3 intentos. El número es", numAleatorio)
