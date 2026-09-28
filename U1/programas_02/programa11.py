print("Dime la hora a la que salió")
hora=int(input())
print("Dime los minutos")
minutos=int(input())
print("Dime los segundos")
segundos=int(input())
print("¿Cuantos segundos tardó en llegar?")
viaje=int(input())
segundosTotales=hora*3600+minutos*60+segundos+viaje
horaLlegada=segundosTotales//3600
minutosLlegada=(segundosTotales%3600)//60
segundosLlegada=(segundosTotales%3600)%60
print(f"Ha llegado a la siguiente hora: {horaLlegada}:{minutosLlegada}:{segundosLlegada}")