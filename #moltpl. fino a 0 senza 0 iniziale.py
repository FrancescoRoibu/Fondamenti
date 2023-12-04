#moltpl. fino a 0 senza 0 iniziale

n = int(input("Dami un numero o '0':"))
x = 1
while n == 0:
    print("Inserisci il primo numero diverso da '0'")
    n = int(input("Dami un numero:"))
while n != 0:
    x = x * n
    n = int(input("Dami un numero o '0':"))
print("Il prodotto è:",x)