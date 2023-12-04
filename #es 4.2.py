#es 4.2

# Somma di tutti i numeri pari tra 2 e 100 (estremi inclusi)
somma_pari = 0
for numero in range(2, 101, 2):
    somma_pari += numero

# Somma di tutti i numeri compresi tra 1 e 100 (estremi inclusi) che sono quadrati perfetti
somma_quadrati_perfetti = 0
for numero in range(1, 101):
    radice_intera = int(numero ** 0.5)
    if radice_intera * radice_intera == numero:
        somma_quadrati_perfetti += numero

# Somma di tutti i numeri dispari compresi tra a e b (estremi inclusi)
a = int(input("Inserisci il valore di a: "))
b = int(input("Inserisci il valore di b: "))
somma_dispari_ab = 0
for numero in range(a, b + 1):
    if numero % 2 != 0:
        somma_dispari_ab += numero

# Somma di tutte le cifre dispari del numero n
n = int(input("Inserisci un numero intero n: "))
somma_cifre_dispari = 0
while n > 0:
    cifra = n % 10
    if cifra % 2 != 0:
        somma_cifre_dispari += cifra
    n //= 10

print("Somma di tutti i numeri pari tra 2 e 100:", somma_pari)
print("Somma di tutti i quadrati perfetti tra 1 e 100:", somma_quadrati_perfetti)
print("Somma di tutti i numeri dispari tra", a, "e", b, ":", somma_dispari_ab)
print("Somma di tutte le cifre dispari del numero n:", somma_cifre_dispari)