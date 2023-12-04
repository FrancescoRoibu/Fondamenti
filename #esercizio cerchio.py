#esercizio cerchio

"""realizzare un prog. che, chieste le coordinate dei centri e i raggi di due cerchi,
controlli se i due cerchi hanno punti in comune"""

import math

# Input delle coordinate dei centri e dei raggi dei due cerchi
x1 = float(input("Inserisci la coordinata x del centro del primo cerchio: "))
y1 = float(input("Inserisci la coordinata y del centro del primo cerchio: "))
r1 = float(input("Inserisci il raggio del primo cerchio: "))

x2 = float(input("Inserisci la coordinata x del centro del secondo cerchio: "))
y2 = float(input("Inserisci la coordinata y del centro del secondo cerchio: "))
r2 = float(input("Inserisci il raggio del secondo cerchio: "))

# Calcolo della distanza tra i centri dei due cerchi
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verifica se i cerchi hanno punti in comune
if d <= r1 + r2:
    print("I due cerchi hanno punti in comune.")
else:
    print("I due cerchi non hanno punti in comune.")