"""
Escribe un programa que realice las siguientes operaciones:
 Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
no se introduzca el número correcto.
 Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
 Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
indica que no quiere continuar el programa finaliza.

"""
continuar=True
while continuar==True:
    num = int(input("Dime un número: "))
    while num<1 or num>10:
        num = int(input("Número incorrecto, debe ser mayor o igual a 1 o menor o igual a 10: "))
    for i in range(1,11):
        resultado = num*i
        print(num," x ",i, " = ",resultado)
    print("¿Deseas introducir un número nuevo?")
    print("1. Si")
    print("2. No")
    opcion = int(input("Dime la opción: "))
    match opcion:
        case 1:
            continuar = True
        case 2:
            continuar = False
