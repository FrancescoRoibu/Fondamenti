#somma con funzioni
l = [1,2,3,4,5]
def somma(l):
    print(l)
    if l == []:
        return 0
    else:
        return l[0] + somma(l[1:])
    
print(somma(l))