#controllare se palindromo

parola = input("Dammi una parola:")

if parola == parola[::-1]:
    print(parola, "è palindroma")
else:
    print("La parola non è palindroma")