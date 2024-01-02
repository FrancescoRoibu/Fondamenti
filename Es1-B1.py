'''
File che contiene n righe contenente parole in italiano.
Una parola per riga.

Realizzare un programma Python che stampi il numero massimo di caratteri (parola di
lunghezza massima) di una parola e tutte le parole con quel numero di caratteri.

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

def maxString(ls):

    massimo = len(ls[0])

    for s in ls:
        if massimo < len(s):
            massimo = len(s)
    return massimo

def cercaParole(ls):

    massimo = maxString(ls)
    print(massimo)

    for s in ls:
        if len(s) == massimo:
            print(s)

file = open_file()

li = lista_cf(file)

cercaParole(li)