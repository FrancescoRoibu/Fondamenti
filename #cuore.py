#cuore

#importiamo turtle
import turtle
#diamo un nome a turtle
cuore = turtle
#impostiamo spessore della penna
cuore.pensize(3)
#definiamo la curva del cuore
def curva_cuore():
    for i in range(200):    #ciclo per disegnare la curva del cuore
        cuore.right(1)    #gira verso destra di 1
        cuore.forward(1)   #va avanti di 1
        
#impostiamo i colori del contorno e del riempimento
cuore.color("black", "red")
#inizio modalità riempimento
cuore.begin_fill()
#prima parte del cuore
cuore.left(140)    #gira verso sinistra di 140 gradi
cuore.forward(112)    #va in avanti di 112 per riuscire a chiudere il cuore
curva_cuore()     #curva del cuore
#seconda parte del cuore
cuore.left(120)    #gira verso sinistra di 120 gradi
curva_cuore()     #curva del cuore
cuore.forward(112)   #va in avanti di 112 per riuscire a chiudere il cuore
#fine modalità riempimento
cuore.end_fill()
#nascondiamo la tartaruga
cuore.hideturtle()
#fine
cuore.done()