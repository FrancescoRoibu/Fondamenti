#trova lettera stringa

s = input("Scrivi una frase:")

trovato = False
i = 0

while(not trovato) and (i < len(s)):
    if s[i] == '2':
        trovato = True
    i = i+1

if trovato:
    print("nella frase :\n", s,"\n c'è z")
else:
    print("nella frase :\n", s,"\n non c'è z")