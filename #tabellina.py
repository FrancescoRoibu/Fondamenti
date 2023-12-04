#tabellina

for i in range(1, 11):
    for j in range (1, 11):
        spazi = " " * (3 - len(str(i*j)))
        print(i * j, spazi, end=" ")
    print("\n")