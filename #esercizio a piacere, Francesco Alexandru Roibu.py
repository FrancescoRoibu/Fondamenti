#disegno a piacere, Francesco Alexandru Roibu

#importiamo Turtle da turtle
from turtle import Turtle
#diamo un nome a Turlte
bandiera = Turtle()
#parte verde
bandiera.begin_fill()
bandiera.forward(100)
bandiera.left(90)
bandiera.forward(200)
bandiera.left(90)
bandiera.forward(100)
bandiera.left(90)
bandiera.forward(200)
bandiera.left(90)
bandiera.fillcolor("green")
bandiera.end_fill()
#parte bianca
bandiera.forward(200)
bandiera.left(90)
bandiera.forward(200)
bandiera.left(90)
bandiera.forward(100)
bandiera.left(90)
bandiera.forward(200)
bandiera.left(90)
#parte rossa
bandiera.begin_fill()
bandiera.forward(200)
bandiera.left(90)
bandiera.forward(200)
bandiera.left(90)
bandiera.forward(100)
bandiera.left(90)
bandiera.forward(200)
bandiera.left(90)
bandiera.fillcolor("red")
bandiera.end_fill()
#input per aspettare un segnale prima di chiudere Python Turtle Graphics
input()