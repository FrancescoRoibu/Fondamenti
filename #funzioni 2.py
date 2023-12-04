#funzioni 2
"""
#calcolo ascissa e ordinata
from math import  *
def cartesiane(distanza, angolo):
    ascissa = distanza * cos(angolo)
    ordinata = distanza * sin(angolo)

    return ascissa, ordinata

r = 10
alfa = pi/3

x, y = cartesiane(r, alfa)
print(x, y)
"""
"""
#disegnare un poligono che disegna un fiore ruotando
from turtle import Turtle
Lato = 100
def poligono(lati):
    for i in range(0, lati):
        tarta.forward(Lato)
        tarta.left(360 / lati)
n = int(input("Lati:"))

tarta = Turtle()
tarta.width()
tarta.color("red")

for i in range(0, n):
    poligono(n)
    tarta.left(360 / n)
"""
#rifare il disegno con le funzioni
