'''
Scrivere una funzione python che ricevendo in ingresso una matrice restituisca
True o False a seconda che la matrice sia la matrice identità o meno

                    1   0   0
Matrice Identità =  0   1   0
                    0   0   1
'''

def verificaMatriceId(matrice):

    dim = len(matrice[0])

    for i in range(dim):
        for j in range(dim):
            if i == j:
                if matrice[i][j] != 1:
                    return False
            else:
                if matrice[i][j] != 0 or matrice[j][i] != 0:
                    return False
    
    return True

m = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m1 = [[1, 0, 0], [0, 1, 0], [0, 3, 1]]

print(verificaMatriceId(m))
print(verificaMatriceId(m1))