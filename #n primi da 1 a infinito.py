#n primi da 1 a n
from math import sqrt
n = int(input("Dammi un numero:"))
for i in range(2, n + 1):
    trovato = False
    for p in range(2, i):
        if i % p == 0:
            trovato = True
            divisore = p
if not trovato:
    print(i, "è primo")