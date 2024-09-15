p1 = int(input('PRIMEIRO TERMO DA PA: '))
r = int(input('RAZÃO DA PA: '))
decimo = p1 + (10 - 1) * r
for i in range(p1, decimo + r, r):
    print(i, end= ' - ')
print('Acabou')