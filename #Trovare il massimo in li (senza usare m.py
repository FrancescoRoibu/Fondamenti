#Trovare il massimo in li (senza usare max)

li = [4, 9, 2, 7, 12, 5]
massimo = li[0]
for elemento in li:
    if elemento > massimo:
        massimo = elemento
print("Massimo elemento in li:", massimo)