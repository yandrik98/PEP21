#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

bisiesto = anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        diasMes = 31
    case 4 | 6 | 9 | 11:
        diasMes = 30
    case 2:
        diasMes = 29 if bisiesto else 28
    case _:
        diasMes = 0  # mes inválido

if anio >= 1 and 1 <= dia <= diasMes:
    print("La fecha es correcta.")
else:
    print("La fecha no es correcta.")