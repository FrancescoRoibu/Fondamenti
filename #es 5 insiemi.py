#chiedere all'utente una frase e verificare se contiene tutte le lettere dell'alfabeto

frase = input("inserisci una frase:")

alfabeto = set('abcdefghijklmnopqrstuvwxyz')

lettere_frase = set()
for carattere in frase:
    lettere_frase.add(carattere)

if alfabeto == lettere_frase:
    print("la frase ha tutte le lettere dell'alfabeto")
else:
    print("la frase non ha tutte le lettere dell'alfabeto")