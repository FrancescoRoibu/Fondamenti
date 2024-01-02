'''
File che contiene n righe contenente parole in italiano.
Una parola per riga.

Realizzare un programma Python che stampi il numero di caratteri delle parole più corte (cioè
con il numero minimo di caratteri) contenute nel file. Il programma deve inoltre stampare tutte 
le parole con quel numero di caratteri.

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

def minString(ls):

    minimo = 1000000000

    for s in ls:
        if minimo > len(s):
            minimo = len(s)
    return minimo

def cercaParole(ls):

    minimo = minString(ls)
    print(minimo)

    for s in ls:
        if len(s) == minimo:
            print(s)

file = open_file()

li = lista_cf(file)

cercaParole(li)