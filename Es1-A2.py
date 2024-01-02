"""
Realizzare un programma Python che, chiedendo all'utente due cifre per l'anno,
stampi tutti i codici fiscali contenenti le due cifre fornite per l'anno.

Il programma deve utilizzare almeno una funzione che, ricevendo come parametro il nome
di un file di codici fiscali, restituisca una lisa con tutti i codici fiscali presenti
nel file.
"""


def open_file():

    nome_file = input("Inserire nome file contenente elenco codici fiscale: ")

    return nome_file


def chiedi_anno():

    anno = input("Inserire le due cifre per l'anno: ")

    return anno


def lista_cf(file):

    lista_output = []

    for line in open(file, 'r').readlines():
        cf = ""
        cf = line.strip()

        lista_output.append(cf)

    return lista_output


def cerca_cf():

    file = open_file()

    anno = chiedi_anno()

    for line in open(file):
        if line[6:8] == anno:
            print(line.strip())


cerca_cf()
