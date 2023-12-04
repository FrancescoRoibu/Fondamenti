#funzioni 3

def fatt(n):
    print("ingresso n:", n)
    if n == 0:
        print("uscita fatt(", n,")=", 1)
        return 1
    else:
        ris = n * fatt(n - 1)
        print("uscita fatt(", n,")=", ris)
        return ris
numero = int(input("Dammi un numero da portare a fattoriale:")) 
fatt(numero)