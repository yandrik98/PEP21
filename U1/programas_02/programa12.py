print("Dime el número de millas")
millas=float(input())
print("Dime el número de km")
km=float(input())
millasAkm = millas*1.61
kmAmillas = km / 1.61
print(round(millasAkm,2))
print(round(kmAmillas,2))