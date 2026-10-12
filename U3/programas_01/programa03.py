"""
Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
similar al siguiente:
1. Calcular el área de un círculo
2. Calcular el área de un triángulo
3. Calcular el área de un rectángulo
4. Salir
Introduce una opción (1-4):
El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la
opción 4.
Hay que diseñar y definir la siguientes funciones: :
 calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y
retorna su área.
 calcular_area_triangulo: recibe como parámetros de entrada la base y la altura
del triangulo y retorna su área.
 calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura
del rectángulo y retorna su área.
 mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.
 main(): lee por teclado la opción seleccionada por el usuario, valida que la opción
está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función
correspondiente en función de la opción seleccionada.
 opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre
sea mayor que 0 y una vez que ha validado el radio llamará a la función
calcular_area_circulo.
 opcion2: descripción: lee por teclado el valor de la base y la altura del triángulo,
valida que los dos datos son mayores que 0 y una vez que los ha validado llamará
a la función calcular_area_triangulo.
 opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que
los dos datos son mayores que 0 y una vez que los ha validado llamará a la función
calcular_area_rectangulo.

"""



def calcular_area_circulo(radio):
    return 3.14 * radio ** 2
def calcular_area_triangulo(base,altura):
    return (base*altura)/2
def calcular_area_rectangulo(base,altura):
    return base * altura
def opcion1():
    radio=float(input("Dime el valor del radio: "))
    while radio <=0:
        radio=float(input("El radio debe ser mayor de 0. Introduce un nuevo valor: "))
    return calcular_area_circulo(radio)
def opcion2():
    base=float(input("Dime la base: "))
    while base<=0:
        base=float(input("La base debe ser mayor de 0. Introduce un nuevo valor: "))
    altura=float(input("Dime la altura: "))
    while altura<=0:
        altura=float(input("La altura debe ser mayor de 0. Introduce un nuevo valor: "))
    return calcular_area_triangulo(base,altura)
def opcion3():
    base=float(input("Dime la base: "))
    while base<=0:
        base=float(input("La base debe ser mayor de 0. Introduce un nuevo valor: "))
    altura=float(input("Dime la altura: "))
    while altura<=0:
        altura=float(input("La altura debe ser mayor de 0. Introduce un nuevo valor: "))
    return calcular_area_rectangulo(base,altura)
def mostrar_menu():
    print("1. Calcular el área de un círculo \n2. Calcular el área de un triángulo \n3. Calcular el área de un rectángulo \n4. Salir")
def main():
    repetir = True
    while repetir == True:
        mostrar_menu()
        opcion=int(input("Introduce una opción (1-4): "))
        while(opcion<1 or opcion>4):
            opcion=int(input("Opcion incorrecta, vuelva a intentarlo: "))
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