def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    while b == 0:
        b = float(input("La b no puede ser 0, introduce un nuevo valor: "))
    return a / b