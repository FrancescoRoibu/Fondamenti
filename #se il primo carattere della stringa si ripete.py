#se il primo carattere della stringa si ripete

s = input("Inserire una frase:")
trovato = False
for i in range(1, len(s)):
    if s[0] == s[i]:
        trovato = True

if trovato:
    print("Il primo carattere si ripete")
else:
    print("Il primo carattere non si ripete")