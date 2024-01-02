'''
Scrivere una funzione in Python con due parametri: un insieme S e una lista T. L'insieme
e la lista contengono numeri interi. La funzione deve togliere dall'insieme S ogni 
valore presente in T.
'''

def cancellaElementi(S, T):

    for i in range(len(T)):
        if T[i] in S:
            S.discard(T[i])
    
    return S

S = {1, 2, 3}
T = [2, 1]

print(cancellaElementi(S, T))