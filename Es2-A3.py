'''
Scrivere una funzione python che ricevendo in ingresso una matrice restituisca
True o False a seconda che la matrice sia simmetrica o meno.

    3  2  1
m = 2  4  0
    1  0  5  
'''

def verificaMatriceSimmetrica(matrice):

    dim = len(matrice[0])
    j = 0

    for i in range(dim - 1):
        j = i + 1
        while j < dim:
            if matrice[i][j] != matrice[j][i]:
                return False
            else:
                j = j + 1

    return True
    

m = [[3, 2, 1], [2, 4, 0], [1, 1, 5]]
m1 = [[1, 1, 1], [1, 2, 1], [1, 1, 3]]

print(verificaMatriceSimmetrica(m))
print(verificaMatriceSimmetrica(m1))