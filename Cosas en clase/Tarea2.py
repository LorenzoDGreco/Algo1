#listaTot = [x**1 for x in range(1,6), x**2 for x in range(1,6), x**2 for x in range(1,6)]
#print(listaTot)

l_terna = []
for x in range(1,6):
    l_terna.append([x,x**2,x**3])

print(l_terna)

listaTot = [[x,x**2,x**3] for x in range(1,6)]
print(listaTot)
