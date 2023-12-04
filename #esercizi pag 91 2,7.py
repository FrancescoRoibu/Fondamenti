#esercizi pag 91 2,7
from math import pi
#input raggio
RAGGIO = int(input("raggio della circonferenza:"))
#calcoli cerchio
AREA_CERCHIO= (pi * (RAGGIO ** 2))
CIRCONFERENZA_CERCHIO = (2 * pi * RAGGIO)
#calcoli sfera
VOLUME_SFERA = 4 / (3 * pi * (RAGGIO ** 3))
AREA_SUPERFICIALE = (4 * pi * (RAGGIO ** 2))
#stampa risultati
print("area cerchio:", AREA_CERCHIO, "cm")
print("circonferenza cerchio:", CIRCONFERENZA_CERCHIO, "cm")
print("volume sfera:", VOLUME_SFERA, "cm")
print("area superficiale:", AREA_SUPERFICIALE, "cm")