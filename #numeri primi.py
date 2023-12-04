#numeri primi

"""
leggi n
per tutti i numeri m minori di n
    se m è primo
        stampa m
"""

n = int(input("Dammi un numero:"))
trovato = False
for i in range(2, n):
    if n % i == 0:
        trovato = True
if trovato:
    print(n, "non è un numero primo")
else:
    print(n, "è un numero primo")

#miglioramento
"""
from math import sqrt
n = int(input("Dammi un numero:"))
trovato = False
for i in range(2, int(sqrt(n)+1):
    if n % i == 0:
        trovato = True
if trovato:
    print(n, "non è un numero primo")
else:
    print(n, "è un numero primo")
"""