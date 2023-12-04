#stampare tutte le lettere dell'alfabeto

#ord si utilizza per trovare il codice ascii
#chr si utilizza per trovare la lettera

carattere = "A"
o = ord(carattere)

for i in range(26):
    print(chr(o + i))