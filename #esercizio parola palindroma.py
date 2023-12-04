#esercizio parola palindroma

s = input("Inserisci una parola:")

t = s[::-1]

if t == s:
    print("La frase è palindroma")
else:
    print("La frase non è palindroma")