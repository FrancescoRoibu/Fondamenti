#lezione 12

"""scrivere un programma che simuli mille lanci di un dado e che al termine si stampi, per ogni faccia del dado,
quante volte è uscita"""
#importiamo random
import random
#impostiamo variabili dado a 0
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
cont6=0
#ciclo for
for i in range(0,1000):
    dado=random.randint(1,6)
    print(dado)   #stampa di tutti i valori del dado
    if dado==1:
        cont1+=1
    elif dado==2:
        cont2+=1
    elif dado==3:
        cont3+=1
    elif dado==4:
        cont4+=1
    elif dado==5:
        cont5+=1
    else:
        cont6+=1
#stampa dei numeri usciti n volte
print("Il numero 1 è uscito",cont1,"volte.")
print("Il numero 2 è uscito",cont2,"volte.")
print("Il numero 3 è uscito",cont3,"volte.")
print("Il numero 4 è uscito",cont4,"volte.")
print("Il numero 5 è uscito",cont5,"volte.")
print("Il numero 6 è uscito",cont6,"volte.")