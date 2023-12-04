#conta le occorrenze

parola = input("Dammi una parola:")
lettera = input("Dammi una lettera:")
conteggio = 0
for i in parola:
    if i == lettera:
        conteggio += 1
print(conteggio)