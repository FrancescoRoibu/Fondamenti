#esercizio 3 valori

"media, valore minimo, valore massimo"
#input interi dei valori
VALORE_1 = int(input("Valore 1:"))
VALORE_2 = int(input("Valore 2:"))
VALORE_3 = int(input("Valore 3:"))
#calcolo media, valore min, valore max e mediana
MEDIA = ((VALORE_1 + VALORE_2 + VALORE_3) / 3)
VALORE_MIN = min(VALORE_1, VALORE_2, VALORE_3)
VALORE_MAX = max(VALORE_1, VALORE_2, VALORE_3)
MEDIANA = ((VALORE_1 + VALORE_2 + VALORE_3) - (VALORE_1 + VALORE_3))
#stampa dei valori calcolati
print("Media:", MEDIA)
print("Valore min:", VALORE_MIN)
print("Valore_max:", VALORE_MAX)
print("Mediana:", MEDIANA)