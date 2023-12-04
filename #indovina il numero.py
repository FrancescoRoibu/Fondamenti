#indovina il numero

import random

numero = random.randint(1,100)
numero_dato = int(input("Indovina il numero:"))

while numero_dato != numero:
    print("Non è il numero coretto")
    numero_dato = int(input("Indovina il numero:"))

print("Hai indovinato")