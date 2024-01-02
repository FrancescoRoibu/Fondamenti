'''
Scrivere una funzione python che ricevendo in ingresso una matrice restituisca
True o False a seconda che la matrice sia composta dai soli valori 1 e -1.

'''

def verificaMatriceZeroMenoUno(matrice):

    dim = len(matrice[0])

    for i in range(dim):
        for j in range(dim):
            if matrice[i][j] != 1 and matrice[i][j] != -1:
                    return False
    
    return True

m = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
m1 = [[1, 1, -1], [1, 1, -1], [-1, -1, 1]]

print(verificaMatriceZeroMenoUno(m))
print(verificaMatriceZeroMenoUno(m1))