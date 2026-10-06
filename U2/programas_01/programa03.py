"""Escribe un programa que pida dos numero y muestre su división. Se deben tener en
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso."""
num1=int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("El numero 2 no puede ser 0")