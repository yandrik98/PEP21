"""
Modifica el programa anterior para que solo se importen las funciones del módulo math
que se usan en el programa.
"""

from math import sin, cos, sqrt, pow

repetir = True
while repetir == True:
    print("1. Seno de un ángulo \n2. Coseno de ángulo \n3. Raíz cuadrada de un número\n4. Potencia de dos números\n5. Salir")
    opcion = int(input("Introduce una opción (1-5): "))
    while opcion < 1 or opcion > 5:
        opcion = int(input("Opcion incorrecta, vuelva a intentarlo: "))
    match opcion:
        case 1:
            angulo = float(input("Dime el ángulo: "))
            seno = sin(angulo)
            print(f"El seno de {angulo} es {seno}")
        case 2:
            angulo = float(input("Dime el ángulo: "))
            coseno = cos(angulo)
            print(f"El coseno de {angulo} es {coseno}")
        case 3:
            num = float(input("Dime un número: "))
            raiz = sqrt(num)
            print(f"La raíz de {num} es {raiz}")
        case 4:
            base = float(input("Dime la base: "))
            exponente = float(input("Dime el exponente: "))
            potencia = pow(base, exponente)
            print(f"La potencia de {base} elevado a {exponente} es {potencia}")
        case 5:
            repetir = False
