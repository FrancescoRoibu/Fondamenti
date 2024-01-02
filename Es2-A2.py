'''
Scrivere una funzione python che ricevendo in ingresso una matrice restituisca
True o False a seconda che la matrice sia composta dai soli valori 0 e 1.

'''

def verificaMatriceZeroUno(matrice):

    dim = len(matrice[0])

    for i in range(dim):
        for j in range(dim):
            if matrice[i][j] != 1 and matrice[i][j] != 0:
                    return False
    
    return True

m = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
m1 = [[1, 0, 0], [0, 1, 0], [0, 3, 1]]

print(verificaMatriceZeroUno(m))
print(verificaMatriceZeroUno(m1))