#es 3 funzioni

#defnire funzione fattori
    #coprimi(n, m)
    #A = fattori (n)
    #B = fattori (m)
    #se A intersezione B = 0
        #ritorna true
    #altrimenti:
        #ritorna false

def fattori(n):
    ris = set()
    for i in range(2, n+1):
        if n % i == 0:
            ris.add(i)
    return ris

def coprimi(n, m):
    A = fattori(n)
    B = fattori(m)
    if A.intersection(B) == set():    #oppure, return A.intersection(B) == set() 
        return True
    else:
        return False

