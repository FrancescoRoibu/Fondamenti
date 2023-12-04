# Cancellare tutte le stringhe più lunghe di 6 caratteri da ls
#(sbagliato)
ls = ["casa", "albero", "gatto", "strada", "albicocca", "francesco"]
for stringa in ls:
    if len(stringa) <= 6:
        stringhe_corte = stringa
        print("Stringhe rimanenti in ls:", stringhe_corte)