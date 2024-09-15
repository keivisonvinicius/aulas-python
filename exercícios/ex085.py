total = [[], []]
valor = 0
for i in range(1,8):
    valor = int(input(f'Digite o {i}o valor: '))
    if valor % 2 == 0:
        total[0].append(valor)
    else:
        total[1].append(valor)
        
total[0].sort()
total[1].sort()  

print(f'valores pares digitados: {total[0]}')
print(f'valores impares digitados: {total[1]}')