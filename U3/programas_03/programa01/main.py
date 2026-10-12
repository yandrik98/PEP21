import operaciones

num1 = float(input("Dime el primer número: "))
num2 = float(input("Dime el segundo número: "))
suma = operaciones.suma(num1,num2)
resta = operaciones.resta(num1,num2)
multiplicacion = operaciones.multiplicacion(num1,num2)
division = operaciones.division(num1,num2)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")