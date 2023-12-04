#carattere maggiore di "m"

n = input("Dammi una parola:")
n.lower()
Trovato = False

for i in n:
    if i > "m":
        Trovato  = True

if Trovato:
    print("La parola ha una lettera maggiore di 'm'")
else:
    print("La parola non contiene una lettera maggiore si 'm'")