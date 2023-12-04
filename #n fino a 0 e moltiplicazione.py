#l'utente fornisce dei numeri fino a 0, poi vanno moltiplicati e stampati

n = int(input("Dami un numero o '0':"))
x = 1
while n != 0:
    x = x * n
    n = int(input("Dami un numero o '0':"))
print("Il prodotto è:",x)