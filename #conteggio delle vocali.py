#conteggio delle vocali

#scrivi una funzione che accetti una stringa come input e restituisca il conteggio delle vocali presenti.

parola = input("Scrivi una parola:")
vocali = "aeiouAEIOU"
conteggio = 0

for elemento in range(len(parola)):
    if parola[elemento] in vocali:
        conteggio += 1

print("il numero di vocali nella stringa è:", conteggio)