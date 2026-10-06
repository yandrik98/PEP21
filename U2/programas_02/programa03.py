"""
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue.
""" 
print("Primera Forma")
for i in range (1,11):
    if i%2==0:
        print(i)
print("Segunda Forma") 
cont=0
while cont<=10:
    cont=cont+1 
    if cont%2==0:
        print(cont)
    

print("Sentencia continue")
print("Tercera Forma")
cont2 = 0
while cont2<10:
    cont2 = cont2 + 1
    if cont2 % 2 != 0:
       continue
    print(cont2)

print("Cuarta Forma")
for a in range(1,11):
    if a%2 != 0:
        continue
    print(a)