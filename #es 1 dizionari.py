#chiedere all'utente una lisa di nomi di persone e poi, mostrando un nome la volta, chiedere l'eta
#relativa alla persona con quel nome.
#creare un dizionario E con coppie nome/eta

nomi = input("Dammi nomi di persona separati da uno spazio:")
nomi_list = []
dizionario_eta = {}
nome1 = ""
for i in nomi:
    if i != " ":
        nome1 += i
    else:
        nomi_list.append(nome1)
        nome1 = ""
if nome1:
    nomi_list.append(nome1)

for nome in nomi_list:
    età = input(f"Dammi l'età di {nome}:")
    dizionario_eta[nome] = età

print("Il dizionario delle età è:", dizionario_eta)