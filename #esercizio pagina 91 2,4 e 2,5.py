#esercizio pagina 91 2,4

#input dei 2 numeri
NUMERO_1 = int(input("numero 1:"))
NUMERO_2 = int(input("numero 2:"))
#operazioni tra i due numeri
SOMMA = NUMERO_1 + NUMERO_2 
DIFFERENZA = NUMERO_1 - NUMERO_2
PRODOTTO = NUMERO_1 * NUMERO_2 
VALOR_MEDIO = (NUMERO_1 + NUMERO_2) / 2
DISTANZA = abs(NUMERO_1 - NUMERO_2)
VALORE_MAX = max(NUMERO_1, NUMERO_2)
VALORE_MIN = min(NUMERO_1, NUMERO_2)
#stampa dei risultati in colonna
values = [SOMMA, DIFFERENZA, PRODOTTO, VALOR_MEDIO, DISTANZA, VALORE_MAX, VALORE_MIN]
valLables = ['somma','differenza','prodotto','valor medio','distanza','valore max','valore min'] 
maxLen = 20
for i in range(len(valLables)):
    print(valLables [i] + ':', end="")
    for j in range(maxLen - len(valLables[i]) - len(str(values[i]))):
        print(' ', end="")
    print(values[i])