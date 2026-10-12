"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor.
"""

def calcular_area_circulo(radio):
    return 3.14 * radio ** 2
def calcular_area_triangulo(base,altura):
    return (base*altura)/2
def calcular_area_rectangulo(base,altura):
    return base * altura
def opcion1():
    valido=False
    while valido==False:
        try:
            radio=float(input("Dime el radio: "))
            if radio<=0:
                print("El radio debe ser mayor de 0.")
            else:
                valido=True
        except ValueError:
            print("Debes introducir un número.")
    return calcular_area_circulo(radio)
def opcion2():
    valido=False
    while valido==False:
        try:
            base=float(input("Dime la base: "))
            if base<=0:
                print("La base debe ser mayor de 0.")
            else:
                valido=True
        except ValueError:
            print("Debes introducir un número.")
    valido=False
    while valido==False:
        try:
            altura=float(input("Dime la altura: "))
            if altura<=0:
                print("La altura debe ser mayor de 0.")
            else:
                valido=True
        except ValueError:
            print("Debes introducir un número.")
    return calcular_area_triangulo(base,altura)
def opcion3():
    valido=False
    while valido==False:
        try:
            base=float(input("Dime la base: "))
            if base<=0:
                print("La base debe ser mayor de 0.")
            else:
                valido=True
        except ValueError:
            print("Debes introducir un número.")
    valido=False
    while valido==False:
        try:
            altura=float(input("Dime la altura: "))
            if altura<=0:
                print("La altura debe ser mayor de 0.")
            else:
                valido=True
        except ValueError:
            print("Debes introducir un número.")
    return calcular_area_rectangulo(base,altura)
def mostrar_menu():
    print("1. Calcular el área de un círculo \n2. Calcular el área de un triángulo \n3. Calcular el área de un rectángulo \n4. Salir")
def main():
    repetir = True
    while repetir == True:
        mostrar_menu()
        valido=False
        while valido==False:
            try:
                opcion=int(input("Introduce una opción (1-4): "))
                if opcion<1 or opcion>4:
                    print("Opción incorrecta, debe estar entre 1 y 4.")
                else:
                    valido=True
            except ValueError:
                print("Debes introducir un número entero.")
        match opcion:
            case 1:
                print("El área del círculo es:",opcion1())
            case 2:
                print("El área del triángulo es:",opcion2())
            case 3:
                print("El área del rectángulo es:",opcion3())
            case 4:
                repetir = False
main()