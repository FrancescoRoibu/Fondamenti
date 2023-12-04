#esercizio  automobile  pag 91 2,10 Completo

"""costo automobile, costo per litro carburante,
km percorsi in un anno, km percorsi per litro carrburante,
valore automobile dopo 5 anni,calcolare i costi totali dopo 5 anni"""
#input di dati dall'utente
COSTO_AUTOMOBILE = int(input("Costo automobile:"))
COSTO_LITRO_CARBURANTE = float(input("Costo litro carburante:"))
KM_PERCORSI_ANNO = int(input("Km percorsi in un anno:"))
KM_PER_LITRO = int(input("Km per litro:"))
VALORE_UTOMOBILE_DOPO_5_ANNI = int(input("Valore dell'auto dopo 5 anni:"))
#calcolo delle varie variabili
COSTO_PER_KM = (COSTO_LITRO_CARBURANTE / KM_PER_LITRO)
COSTO_KM_1ANNO = (KM_PERCORSI_ANNO * COSTO_PER_KM)
COSTO_5ANNI = (COSTO_KM_1ANNO * 5)
TOTALE = (COSTO_AUTOMOBILE + COSTO_5ANNI - VALORE_UTOMOBILE_DOPO_5_ANNI)
#stampa del costo totale
print("Costo totale dopo 5 anni:", TOTALE)