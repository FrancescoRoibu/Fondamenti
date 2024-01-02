'''
File che contiene n righe contenente parole in italiano.
Una parola per riga.

Realizzare un programma Python che stampi tutte le parole con un numero di caratteri superiore 
alla media.

Il programma deve prevedere almeno una funzione che, ricevendo come parametro il nome
di un file contenente parole italiane restituisca una lista di tutte le parole presenti.
'''

def open_file():

    nome_file = input("Inserire nome file contenente elenco parole: ")

    return nome_file


def lista_cf(file):

    lista_output = []

    for line in open(file, 'r').readlines():
        cf = ""
        cf = line.strip()

        lista_output.append(cf)

    return lista_output

def mediaString(ls):

    somma = 0
    media = 0

    for s in ls:
        somma = somma + len(s)

    media = round(somma / len(ls))

    return media

def cercaParole(ls):

    media = mediaString(ls)
    print(media)

    for s in ls:
        if len(s) > media:
            print(s)

file = open_file()

li = lista_cf(file)

cercaParole(li)