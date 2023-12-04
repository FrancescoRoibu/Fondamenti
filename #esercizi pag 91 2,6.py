#esercizi pag 91 2,6

#input misura in metri
MISURA = int(input("misura espressa in metri:"))
#calcoli per la conversione
METRI_MIGLIA = (MISURA * (6 * 10 ** -3))
METRI_PIEDI = (MISURA * 3,281)
METRI_POLLICI = (MISURA * 39,3701)
#stampa dei risultati
print("metri a miglia:", METRI_MIGLIA)
print("metri a piedi:", METRI_PIEDI)
print("metri a pollici:", METRI_POLLICI)