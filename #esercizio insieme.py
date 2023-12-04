#esercizio insieme

#scrivere un programma che costruisca gli insiemi X dei quadrati minori
#di 1000 e l'insieme Y dei cubi minori di 1000 e verifichi se esiste un
#naturale il cui predecessore è un quadrato e il cui successore è un cubo.
limite = int(input("Dammi un limite:"))
numero = 1
X = set()
quadrato = numero * numero
while quadrato <= limite:
    X.add(quadrato)
    numero = numero + 1
    quadrato= numero * numero

numero = 1
Y = set()
cubo = numero ** 3
while cubo <= limite:
    Y.add(cubo)
    numero = numero + 1
    cubo = numero ** 3

print("Quadrati:", X)
print("Cubi", Y)

for n in range(1, limite+1):
    if (n-1 in X) and (n+1 in Y):
        print("Numero naturale:", n)

print("Fine")