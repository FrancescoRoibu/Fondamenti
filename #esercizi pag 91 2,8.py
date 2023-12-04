#esercizi pag 91 2,8
from math import sqrt
#input lati
LATO_1 = int(input("lato 1 del rettangolo:"))
LATO_2 = int(input("lato 2 del rettangolo:"))
#calcoli
AREA = (LATO_1 * LATO_2)
PERIMETRO = 2 * (LATO_1 + LATO_2)
DIAGONALE = sqrt ((LATO_1 ** 2) + (LATO_2 ** 2))
#stampa risultati
print("area:", AREA)
print("perimetro:", PERIMETRO)
print("diagonale:", DIAGONALE)