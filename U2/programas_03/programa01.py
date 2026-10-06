incorrecto = True

while incorrecto == True:
    try:
        num = int(input("Introduce un número entre 1 y 10: "))
    except ValueError:
        print('Debes introducir números')
    else:
        if num >= 1 and num <= 10:
            incorrecto = False
        else:
            print("Número incorrecto, debe estar entre 1 y 10.")

print(f"Has introducido el número {num}")