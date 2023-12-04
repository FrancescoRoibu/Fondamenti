#es p4.2 pag 243

"""leggi n
mentre n >= 0

leggi n"""

"""leggi n
minimo = n
mentre n >= 0
    se n < minimo
        minimo = n
    leggi n
stampa minimo"""

n = int(input("Dammi un numero naturale:"))

pari = " "
dispari = " "
somma = 0
minimo = n
massimo = n
media = 0
conto = 0
precedente = n
valori_adiacenti_duplicati = " "
while n >= 0:
    somma = somma + n
    conto = conto + 1
    media = somma / conto
    if n < minimo:
        minimo = n
    if n > massimo:
        massimo = n
    if n % 2 == 0:
        pari = pari + str(n) + " "
    else:
        dispari = dispari + str(n) + " "
    if n == precedente:
        valori_adiacenti_duplicati += str(n) + " "
    precedente = n
    n = int(input("Dammi un numero naturale:"))

print("Il minimo è:", minimo)
print("Il massimo è:", massimo)
print("I pari sono:", pari)
print("I dispari sono:", dispari)
print("La somma dei numeri è:", somma)
print("La media è:", media)
print("Valori adiacenti duplicati:", valori_adiacenti_duplicati)