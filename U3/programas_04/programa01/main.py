# imports de la librería estándar

# imports de librerías de terceros

# imports de módulos propios
from matematicas import figuras, operaciones


# Definición de funciones principales
def menuOperaciones():
    num1 = float(input("Dime el primer número: "))
    num2 = float(input("Dime el segundo número: "))
    suma = operaciones.suma(num1, num2)
    resta = operaciones.resta(num1, num2)
    multiplicacion = operaciones.multiplicacion(num1, num2)
    division = operaciones.division(num1, num2)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")


def menuAreas():
    print("1. Rectángulo \n2. Triángulo \n3. Círculo")
    figura = int(input("Elige una figura (1-3): "))
    while figura < 1 or figura > 3:
        figura = int(input("Opción incorrecta, vuelva a intentarlo: "))

    match figura:
        case 1:
            base = float(input("Dime la base: "))
            altura = float(input("Dime la altura: "))
            areaR = figuras.area_rectangulo(base, altura)
            print(f"Área del rectángulo: {areaR}")
        case 2:
            base = float(input("Dime la base: "))
            altura = float(input("Dime la altura: "))
            areaT = figuras.area_triangulo(base, altura)
            print(f"Área del triángulo: {areaT}")
        case 3:
            radio = float(input("Dime el radio: "))
            areaC = figuras.area_circulo(radio)
            print(f"Área del círculo: {areaC}")


def main():
    """Función principal del programa"""
    repetir = True
    while repetir == True:
        print("1. Operaciones matemáticas \n2. Cálculo de áreas geométricas \n3. Salir")
        opcion = int(input("Introduce una opción (1-3): "))
        while opcion < 1 or opcion > 3:
            opcion = int(input("Opción incorrecta, vuelva a intentarlo: "))

        match opcion:
            case 1:
                menuOperaciones()
            case 2:
                menuAreas()
            case 3:
                repetir = False


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()