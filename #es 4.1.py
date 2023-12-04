n = int(input("Inserisci un numero intero n: "))

num = 1
quadrati = " "
divisori = " "
potenze = " "

while num<= n:
    if num * num < n:
        quadrati += str(num * num) + " "
    if num % 10 == 0:
        divisori += str(num) + " "
    if (num & (num - 1)) == 0 and num != 0:
        potenze += str(num) + " "
    num += 1

print("quadrati di", n,":", quadrati)
print("divisori di", n,":", divisori)
print("potenze di", n,":", potenze)