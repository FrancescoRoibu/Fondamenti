#esercizi pag 91 2,10

#valori di input
COSTO_AUTOMOBILE = int(input("costo automobile:"))
MIGLIA_PERCORSE = int(input("miglia percorse ogni anno:"))
COSTO_CARBURANTE = float(input("costo carburante:"))
#calcolo consumo carburante
COSTO_CARBURANTE_AUTO_CONVENZIONALE = (MIGLIA_PERCORSE * COSTO_CARBURANTE)
COSTO_CARBURANTE_AUTO_IBRIDA = (MIGLIA_PERCORSE * 0.6 * COSTO_CARBURANTE)
#risparmio
RISPARMIO_ANNUO = (COSTO_CARBURANTE_AUTO_CONVENZIONALE - COSTO_CARBURANTE_AUTO_IBRIDA)
#tempo ammortamento
TEMPO_AMMORTAMENTO = (COSTO_AUTOMOBILE / RISPARMIO_ANNUO)
#stampa risultati
print("costo carburante auto convenzionale:", COSTO_CARBURANTE_AUTO_CONVENZIONALE, "euro")
print("costo carburante auto ibrida", COSTO_CARBURANTE_AUTO_IBRIDA, "euro")
print("risparmio annuo:", RISPARMIO_ANNUO, "euro")
print("trmpo ammortamento:", TEMPO_AMMORTAMENTO, "euro")
#scelta dell'auto
if TEMPO_AMMORTAMENTO < 5:
    print("si consiglia l'auto ibrida")
else:
    print("si consiglia l'auto convenzionale")