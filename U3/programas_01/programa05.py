"""
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).

"""



g = "pruebaGlobal1" #variable global
def funcionGlobal():
    global g #cojo la variable global
    g = "pruebaGlobal2" #modifico la variable global, pasa de ser prueba1 a prueba2
    print("Variable modificada",g)
def funcionLocal():
    g = "local"
    print(g)
    print("La variable", g , "solo funciona en esta funcion, fuera no")
def funcionNonLocal():
    g="pruebaNonLocal1"
    print(g)
    def funcionNonLocalInterna():
        nonlocal g #coge la variable de la función externa
        g = "pruebaNonLocal2" #Fue modificada
    funcionNonLocalInterna()
    print("Variable modificada", g)
def main():
    print("Global al principio:", g)
    funcionLocal()
    print("Global tras funcionLocal:", g)
    funcionGlobal()
    print("Global tras funcionGlobal:", g)
    funcionNonLocal()
    print("Global tras funcionNonLocal:", g)

main()