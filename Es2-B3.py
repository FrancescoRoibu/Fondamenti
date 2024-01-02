'''
Scrivere una funzione in Python con due parametri: una tupla t1 e una tupla t2. Le tuple hanno
un numero uguale di elementi che sono numeri interi.
La funzione deve restituire una lista in cui ciascun elemento è la somma degli elementi corrispondenti
in t1 e t2.
'''

def sommaElementiTuple(t1, t2):

    res = []

    for i in range(len(t1)):
        res.insert(i, t1[i] + t2[i])
    
    return res

t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(sommaElementiTuple(t1, t2))