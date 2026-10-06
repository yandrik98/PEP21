"""
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente.

""" 
num=int(input("Dime un número: "))
while num<1 or num>10:
    num=int(input("Número introducido incorrectamente, vuelva a intentarlo: "))