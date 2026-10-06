"""Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
negativo) y si el valor no es correcto, mostrará un aviso."""

par = int(input("Dime un número par: "))
if (par%2==0):
    impar = int(input("Dime un número impar: "))
    if(impar%2 == 0):
        print("El número no es impar")
else:
    print("El número no es par")