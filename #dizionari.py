#dizionari
"""
valori = {1: "uno", 2: "due", 3: "tre", 4: "quattro", 5: "cinque"}
n = 3
v3 = valori[3] #valore di 3
print(v3)
v5 = valori[5] #valore di 5
print(v5)
#cambiamp valore di 1 da uno ad UNO
valori[1] = "UNO"
print(valori)
#nuovo valore
valori[6] = "sei"
print(valori)
#srivere tutti i valori in maiuscolo
for i in range(1,7):
    valori[i] = valori[i].upper()
print(valori)

#lista di parole: parole = ["casa", "dolce", "casa"]
frase = input("scrivi una frase:")    #utente da la frase
parole = frase.split() #data una stringa separa le parole
conteggio = {}   #dizionario vuoto
for p in parole:
    if p in conteggio:
        conteggio[p] = conteggio[p] + 1
    else:
        conteggio[p] = 1
print(conteggio)
"""
