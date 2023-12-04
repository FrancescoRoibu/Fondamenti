#controllare se in li ci sono elementi ripetuti

li = [3, 5, 3, 7, 9, 10]
ha_ripetuti = False
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] == li[j]:
            ha_ripetuti = True
if ha_ripetuti:
    print("Ci sono elementi ripetuti in li.")
else:
    print("Non ci sono elementi ripetuti in li.")