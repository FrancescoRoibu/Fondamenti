'''
Scrivere una funzione in Python con due parametri: un dizionario d ed un valore n.
Il dizionario ha come chiavi nomi di studenti e come valori i voti presi ad un esame.
La funzione deve stampare tutti i nomi degli studenti cha abbiano conseguito un voto
maggiore di n.
'''

def stampaNomi(d, n):

    for nome, voto in d.items():
        if d[nome] > n:
            print(nome)

studenti = {'pippo':30, 'pluto':20, 'minni':30, 'clarabella':25}  

stampaNomi(studenti, 25)