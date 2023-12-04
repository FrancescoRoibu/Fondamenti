#numero contiene 7?

numero = int(input("Inserire un numero intero:"))

numero_str = str(numero)

if '7' in numero_str:
    print("il numero", numero, "contiene la cifra 7")
else: 
    print("in numero", numero, "non contiene la cifra 7")