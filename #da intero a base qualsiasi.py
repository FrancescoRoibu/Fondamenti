#da intero a base qualsiasi

n = int(input("Inserire un numro intero:"))
base = int(input("Inserisci una base:"))
stringa = ""
q = n

while n < 0:
    print("non se po fa amico")
    n = int(input("Inserire un numro intero:"))
while (q != 0):
    q = n // base
    r = n % base
    n = q
    stringa = stringa + str(r)

    print(stringa[::-1])   #scrive la stringa al contrario