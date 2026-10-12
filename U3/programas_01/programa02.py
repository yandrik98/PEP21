"""
Escribe un programa en Python que haga uso de una función llamada saludar que cumpla
los siguientes requisitos:
 Entrada: Tiene 4 parámetros de entrada, que serán 4 cadenas de texto: nombre,
primer apellido, segundo apellido y curso. El parámetro curso tendrá en la
declaración de la función el valor por defecto “2DAW”
 Salida: No tiene parámetros de salida.
 Funcionalidad: Imprime por pantalla un mensaje saludando al alumno/a que se
haya pasado como parámetro de entrada.
El programa debe invocar a la función varias veces. En algunas de ellas se tiene que usar
el paso de parámetros de forma nominal (con clave valor).
"""



def saludar(nombre,apellido1,apellido2,curso="2DAW"):
    print("Bienvenido/a,",nombre,apellido1,apellido2,". Curso:",curso)

nombre = input ("Dime tu nombre: ")
apellido1 = input ("Dime tu primer apellido: ")
apellido2 = input ("Dime tu segundo apellido: ")
curso = "1DAW"
saludar(nombre,apellido1,apellido2)
saludar(nombre,apellido1,apellido2,curso="ASIR")
saludar(apellido1="Pérez" , nombre = "Lucas", apellido2="Gómez", curso=curso)
