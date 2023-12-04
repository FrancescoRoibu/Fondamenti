#è un numero perfetto o no?
#inizializza variabili
n = int(input("Dammi un numero naturale:"))
s = 0
#itera sui numeri da 1 a n/2(escludendo n)
for i in range(1, (n//2) + 1):   #n//2 perchè il divisore massimo è la metà di n
    #se i è un divisore di n, si aggiunge alla somma
    if n % i == 0:
        s = s + 1
    #se la somma dei divisori è uguale a n, allora n è un numero perfetto

if n == s:
    print("è un numero perfetto")
else:
    print("NON è un numero perfetto")