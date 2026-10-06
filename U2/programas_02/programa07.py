"""
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no.

""" 
#Version2
suma = 0
cont = 0
num = int(input("Dime un número: "))
while num != 0:
    suma = suma + num
    cont = cont + 1
    num = int(input("Dime un número: "))
print("Suma", suma)
print("Media", suma/cont)
