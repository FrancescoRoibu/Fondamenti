#2 dadi 1000 volte

#importiamo random
import random
#impostiamo variabili dado1 a 0
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
cont6=0
#impostiamo variabili dado2 a 0
cont1_2=0
cont2_2=0
cont3_2=0
cont4_2=0
cont5_2=0
cont6_2=0
#impostiamo variabile coppie uguali a 0
coppie_uguali = 0
#ciclo for
for i in range(0,1000):
    dado=random.randint(1,6)
    dado2=random.randint(1,6)
    #dado1
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
    #dado2
    if dado2==1:
        cont1_2+=1
    elif dado2==2:
        cont2_2+=1
    elif dado2==3:
        cont3_2+=1
    elif dado2==4:
        cont4_2+=1
    elif dado2==5:
        cont5_2+=1
    else:
        cont6_2+=1
    if dado2==dado:
        coppie_uguali+=1
#stampa numeri dado1
print("Il numero 1 è uscito",cont1,"volte.")
print("Il numero 2 è uscito",cont2,"volte.")
print("Il numero 3 è uscito",cont3,"volte.")
print("Il numero 4 è uscito",cont4,"volte.")
print("Il numero 5 è uscito",cont5,"volte.")
print("Il numero 6 è uscito",cont6,"volte.")
#stampa numeri dado2
print("Il numero 1_2 è uscito",cont1_2,"volte.")
print("Il numero 2_2 è uscito",cont2_2,"volte.")
print("Il numero 3_2 è uscito",cont3_2,"volte.")
print("Il numero 4_2 è uscito",cont4_2,"volte.")
print("Il numero 5_2 è uscito",cont5_2,"volte.")
print("Il numero 6_2 è uscito",cont6_2,"volte.")
#stampa numero di volte che è uscita la coppia uguale
print("Numero di volte che è uscita una coppia di valori uguali:", coppie_uguali)