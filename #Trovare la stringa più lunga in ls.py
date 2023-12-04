#Trovare la stringa più lunga in ls

ls = ["ciao", "buongiorno", "salve", "hello"]
lunghezza_massima = 0
stringa_più_lunga = ""
for stringa in ls:
    lunghezza = len(stringa)
    if lunghezza > lunghezza_massima:
        lunghezza_massima = lunghezza
        stringa_più_lunga = stringa
print("La stinga più lunga in ls:", stringa_più_lunga)