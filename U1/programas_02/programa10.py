print("Dime un número de dos cifras")
num1=int(input())
unidades=num1%10
decenas=num1//10
num2=unidades*10+decenas 
print(f"El número invertido es {num2}")