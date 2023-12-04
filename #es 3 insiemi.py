#chiedendo all'utente un insieme di numeri naturali, creare l'insieme dei quadrati
#Q e quello dei cubi C dei numeri dati

numeri = input("Dammi numeri naturali:")
insieme_dei_numeri = set()

while numeri != "stop":
    insieme_dei_numeri.add(numeri)
    numeri = input("Dammi numeri naturali:")

insieme = set()
for elemento in insieme_dei_numeri:
    num = int(elemento)
    insieme.add(num)

insieme_quadrati = set()
insieme_cubi = set()

for numero in insieme:
    cubo = numero ** 3
    insieme_cubi.add(cubo)
    quadrato = numero ** 2
    insieme_quadrati.add(quadrato)

print("insieme dei cubi:", insieme_cubi)
print("insieme dei quadrati:", insieme_quadrati)

#es 4...

intersezione = insieme_quadrati.intersection(insieme_cubi)

if len(intersezione) == 0:
    print("i due insiemi sono disgiunti")
else:
    print("i due insiemi hanno punti in comune")