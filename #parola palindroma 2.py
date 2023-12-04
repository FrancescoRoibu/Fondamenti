#parola palindroma 2

s = input("Dammi una frase:")
trovati_diversi = False
n = len(s)
#ciclo per tutti i valori di i

for i in range(0, n//2 + 1):
    j = n - (i + 1)
    if s[i] != s[j]:
        trovati_diversi = True

if trovati_diversi == False:
    print(s, "\n è palindroma")
else:
    print(s, "\n non è palindroma")