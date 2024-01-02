"""
Realizzare un programma Python che, chiedendo all'utente tre lettere per il cognome,
stampi tutti i codici fiscali contenenti le tre lettere fornite per il cognome.

Il programma deve utilizzare almeno una funzione che, ricevendo come parametro il nome
di un file di codici fiscali, restituisca una lisa con tutti i codici fiscali presenti
nel file.
"""


def open_file():

    nome_file = input("Inserire nome file contenente elenco codici fiscale: ")

    return nome_file


def chiedi_cognome():

    cognome = input("Inserire tre lettere del cognome: ")

    return cognome


def lista_cf(file):

    lista_output = []

    for line in open(file, 'r').readlines():
        cf = ""
        cf = line.strip()

        lista_output.append(cf)

    return lista_output


def cerca_cf():

    file = open_file()

    cognome = chiedi_cognome().upper()

    for line in open(file):
        if line[0:3] == cognome:
            print(line.strip())


cerca_cf()
