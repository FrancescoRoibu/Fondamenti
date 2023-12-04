#lezione 10 

#esercizio robot

"""t1= l1/s1
l2= radq((dx-l1)**2+(dy**2))
t2= l1/s2
risultato= t1+t2

calcolo t1
calcola l2
calcola t2
riporta il tempo totale

va chiesto dx,dy,l1,s1,s2"""

from math import *    #importiamo la funzione sqrt da math

dx = int(input("Distanza direzione x:"))
dy = int(input("Distanza direzione y:"))
l1 = int(input("Lunghezza primo tratto:"))
s1 = int(input("Velocità primo tratto:"))
s2 = int(input("Velocità secondo tratto:"))

t1 = (l1 / s1)  #tempo per percorrere il primo tratto

l2 = sqrt((dx - l1) ** 2 + (dy) ** 2)  #calcolo secondo tratto

t2 = (l2 / s2)  #tempo per percorrere il secondo tratto

risultato = t1 + t2    #tempo totale

print(risultato, "ore")   #stampa risultato