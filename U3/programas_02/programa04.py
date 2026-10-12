"""
El módulo turtle es una biblioteca estándar de Python que permite crear gráficos y dibujos
de manera sencilla, moviendo una “tortuga” virtual por la pantalla. El módulo está instalado
por defecto en el interprete de Python.
Investiga la documentación del módulo https://docs.python.org/3/library/turtle.html y
escribe un programa que:
 Dibuje un cuadrado rojo sin rellenar.
 Dibuje un circulo verde relleno
"""

import turtle

lapiz = turtle.Turtle()

lapiz.color("red")
for i in range(4):
    lapiz.forward(100)
    lapiz.left(90)

lapiz.penup()
lapiz.goto(200, 0)
lapiz.pendown()

lapiz.color("green")
lapiz.begin_fill()
lapiz.circle(50)
lapiz.end_fill()

turtle.done()