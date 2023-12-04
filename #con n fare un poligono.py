#con n fare un poligono

import turtle

# Funzione per disegnare un poligono regolare con n lati
def disegna_poligono(n):
    angolo = 360 / n  # Calcola l'angolo tra i lati del poligono
    for i in range(n):
        turtle.forward(100)  # Lunghezza dei lati del poligono
        turtle.left(angolo)  # Gira di 'angolo' gradi

# Input del numero di lati del poligono
n = int(input("Inserisci il numero di lati del poligono regolare: "))

# Inizializza la tartaruga
turtle.speed(1)  # Imposta la velocità della tartaruga

# Disegna il poligono regolare
disegna_poligono(n)

# Chiudi la finestra alla pressione del mouse
turtle.exitonclick()