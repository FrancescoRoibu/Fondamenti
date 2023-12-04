#if else

#max tra due numeri

m = int(input("primo numero:"))
n = int(input("secondo numero:"))

if m > n: 
    max = m
else:
    max = n

print("valore massimo:", max)

#valore assoluto di un numero

n = int(input("Un numero:"))

if n < 0:
    n = -n 

print("Valore assoluto:", n)

# confronto tra numeri in elif else

m = int(input("Primo numero:"))
n = int(input("Secondo numero:"))

if n < m: 
    print(n, "è minore di", m)
elif n == m:
    print("I numeri sono uguali")
else: 
    print(n, "è maggiore di", m)

# lancia un dado e ne stampa il valore 

import random
faccia = random.randint(1, 6) #lancio del dado

if faccia == 1:
    print("Uno")
elif faccia == 2:
    print("Due")
elif faccia == 3:
    print("Tre")
elif faccia == 4:
    print("Quattro")
elif faccia == 5:
    print("Cinque")
else:
    print("Sei")

