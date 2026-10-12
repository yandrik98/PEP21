"""
Escribe un programa en Python que importe el modulo math completo y que le pregunte al
usuario que operación matemática quiere hacer:
1. Seno de un ángulo
2. Coseno de ángulo
3. Raíz cuadrada de un número
4. Potencia de dos números.
Le pida los datos necesarios y muestre los resultados por pantalla.
"""

import math

repetir = True
while repetir == True:
    print("1. Seno de un ángulo \n2. Coseno de ángulo \n3. Raíz cuadrada de un número\n4. Potencia de dos números\n5. Salir")
    opcion = int(input("Introduce una opción (1-5): "))
    while opcion < 1 or opcion > 5:
        opcion = int(input("Opcion incorrecta, vuelva a intentarlo: "))
    match opcion:
        case 1:
            angulo = float(input("Dime el ángulo: "))
            seno = math.sin(angulo)
            print(f"El seno de {angulo} es {seno}")
        case 2:
            angulo = float(input("Dime el ángulo: "))
            coseno = math.cos(angulo)
            print(f"El coseno de {angulo} es {coseno}")
        case 3:
            num = float(input("Dime un número: "))
            raiz = math.sqrt(num)
            print(f"La raíz de {num} es {raiz}")
        case 4:
            base = float(input("Dime la base: "))
            exponente = float(input("Dime el exponente: "))
            potencia = math.pow(base, exponente)
            print(f"La potencia de {base} elevado a {exponente} es {potencia}")
        case 5:
            repetir = False
