#dati 2 insiemi calcolare la differenza simmetrica, cioè l'insieme degli elementi presenti solo in uno dei 2 insiemi.

ins_1 = {1, 2, 3, 4, 5}
ins_2 = {3, 4, 5, 6, 7}

diff_1 = ins_1 - ins_2
diff_2 = ins_2 - ins_1

differenza_simmetrica = diff_1.union(diff_2)

print(differenza_simmetrica)