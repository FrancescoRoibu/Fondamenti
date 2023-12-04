#lunghezza stringa pari o dispari

parola = input("Dammi una parola:")
lunghezza = len(parola)

if lunghezza % 2 == 0:
    print("La lunghezza della stringa è pari")
else:
    print("La lunghezza della stringa è dispari")