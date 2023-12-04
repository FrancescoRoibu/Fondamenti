#lezione 14

#esercizio p4.7  (scambio caratteri)
#leggi s,i,j
s = input("Dammi una frase:")
i = int(input("Dammi un indice:"))
j = int(input("Dammi un indice maggiore:"))
#se i > j
if i > j:
    k = j
    j = i
    i = k
#calcola A,B,C
A = s[:i]
B = s[i+1:j]
C = s[j+1:]
#calcola t
t = A + s[j] + B + s[i] + C
#calcola s
s = t
#stampa s
print(s)