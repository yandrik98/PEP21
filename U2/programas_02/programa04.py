"""
Escribe un programa que use un bucle while y le pida continuamente al usuario que
introduzca un número hasta que ingrese 45 como la número de salida secreto, en cuyo
caso el mensaje "¡Has dejado el bucle con éxito" debe imprimirse en la pantalla y el bucle
debe terminar.
Haz dos dos versiones del programa:
Programación en Python (PEP) - IES Leonardo Da Vinci - Álvaro García
U2P03-Programas_02. Estructuras repetitivas (bucles)
 Versión 1: Utiliza el concepto de ejecución condicional y la instrucción break. En
este caso el bucle no evaluará ninguna condición, es decir, será un bucle infinito.
 Versión 2: Realmente no es necesario usar la instrucción break. Diseña una
solución donde no se use break y el bucle while controle la condición de salida.
"""
#Version 1
while True:
    num = int(input("Introduce un número: "))
    if num == 45:
        print("¡Has dejado el bucle con éxito!")
        break
#Version 2
num2 = int(input("Dime un número: "))
while num2 != 45:
    num2 = int(input("Número incorrecto, introduce de nuevo un número: "))
print("¡Has dejado el bucle con éxito!")