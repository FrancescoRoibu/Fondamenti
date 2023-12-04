#ricorsione con turtle

from turtle import Turtle
Mindist = 10
t = Turtle(); t.color("red"); t.width(2)

def lato(l):
    print(l)
    if l < Mindist:
        t.forward(l)
    else:
        lato(l/3)
        t.left(60)
        lato(l/3)
        t.right(120)
        lato(l/3)
        t.left(60)
        lato(l/3)

lato(300)