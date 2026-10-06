"""
Escribe un programa que pida un número y muestre una lista de números desde 1 al
número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto.

"""

num = int(input("Dime un número: "))
while num<1 or num>10:
    num = int(input("Número incorrecto, debe ser mayor o igual a 1 o menor o igual a 10: "))
for i in range(1, num + 1):
    print(i)