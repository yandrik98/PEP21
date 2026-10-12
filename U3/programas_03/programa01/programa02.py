# imports de la librería estándar

# imports de librerías de terceros

# imports de módulos propios
import operaciones


# Definición de funciones principales
def main():
    """Función principal del programa"""
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


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    main()