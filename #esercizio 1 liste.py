#esercizio 1 liste

li = []
n = input("Dammi un intero (o STOP):")

while n.upper() != "STOP":
    intero = int(n)
    li.append(intero)
    #oppure li = li + [intero]
    n = input("Dammi un intero (o STOP):")
max = li[0]
for i in li:
    if i > max:
        max = i
print("Il numero  massimo è:", max)

#con indice
"""
for i in range(len(li)):
    if li[i] > max:
        massimo = li[i]
"""

#con sort ( più lento di quello con indice perchè utilizza il metodo lineare)
"""
li.sort()
print(li[-1])
"""