#calcola la somma di numeri inseriti dall'utente

n = int(input("Primo numero della somma:"))
limite = int(input("Limite della somma:"))
somma = 0

while somma <= limite:
    n = int(input("Dammi un'altro numero:"))
    somma = somma + n
print(f"La somma dei numeri inseriti supera {limite}. La somma totale è {somma}")