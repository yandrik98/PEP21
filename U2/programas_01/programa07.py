"""
Escriba un programa que pida un año y que escriba si es bisiesto o no. Un año es bisiesto
si es múltiplos de 4 pero no múltiplos de 100, aunque si los múltiplos de 400.

"""


anio = int(input("Introduce un año: "))

if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")