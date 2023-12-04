# gioco numero 7

n = int(input("numero massimo:"))
spazi = " " * (5 - len(str(n)))
for i in range(1, n):
    if i % 7 == 0 or '7' in str(i):
        print("passo")
    else:
        print(spazi, str(i))