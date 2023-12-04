#cancellare altro metodo

ls = ["casa", "albero", "gatto", "strada", "albicocca", "Francesco"]
minori = []
for s in ls:
    if len(s) <= 6:
        minori.append(s)
ls = minori
print(ls)

"""
ls = ["casa", "albero", "gatto", "strada", "albicocca", "Francesco"]
minori = list(ls)
for s in ls:
    if len(s) > 6:
        minori.remove(s)
print(minori)
"""

"""
ls = ["casa", "albero", "gatto", "strada", "albicocca", "Francesco"]
i = 0
while i < len(ls):
    if len(ls[i]) > 6:
        ls.pop(i)
    else:
        i = i + 1
        
print(ls)
"""