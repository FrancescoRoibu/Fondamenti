#es 3 dizionari

#creare un dizionario D le cui chiavi sono i naturali fino a 100 e ogni
#valore è una lista contenente il quadrato, il cubo, e la quarta potenza della chiave

#crea dizionario vuoto
potenze = {}
#per ogni numero naturale:
    #metti n e la lista [n^2, n^3, n^4] in potenze

for n in range(1, 101):
    potenze[n] = [n*n, n*n*n, n*n*n*n]  #oppure n**2 ecc. ma è più lento
for chiave in potenze:
    print(chiave, ":", potenze[chiave][0], ",", potenze[chiave][1], ",", potenze[chiave][2])
#con [0] stampa i quadrati [1] i cubi e con [2] la quarta potenza