#se si ripetono caratteri nella frase

s = input("Dammi una frase:")

trovato = False
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            trovato = True

if trovato:
    print("La stringa contiene caratteri uguali")
else:
    print("La stringa non contiene caratteri uguali")