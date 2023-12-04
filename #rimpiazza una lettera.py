#rimpiazza una lettera

parola = input("Dammi una parola:")
lettera1 = input("Dammi la lettera da sostituire:")
lettera2 = input("Dammi la lettera con cui cambiarla:")

for i in parola:
    if i == lettera1:
        parola2 = parola.replace(lettera1, lettera2)
print("La parola", parola, "sostituendo", lettera1, "con", lettera2, "è", parola2)