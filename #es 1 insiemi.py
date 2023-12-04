#data una lista, eliminare gli elementi che appaiono due volte o più

nomi = ["giulia", "francesco", "maia", "marianna", "maia", "giulia"]

nomi_duplicati = set()
nomi_unici = []

for nome in nomi:
    if nome in nomi_unici:
        nomi_duplicati.add(nome)
    else:
        nomi_unici.append(nome)
    
for nome in nomi_duplicati:
    while nome in nomi_unici:
        nomi_unici.remove(nome)

print(nomi_unici)