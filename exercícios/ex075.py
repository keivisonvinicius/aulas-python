num = (int(input('Digite um número: ')),int(input('Digite um número: ')), 
       int(input('Digite um número: ')), int(input('Digite um número: '))) 
print(f'Você digitou os valores: {num}')
print(f'o valor nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor três foi digitado primeiro na posição {num.index(3)+1}')
else:
    print('o valor não foi digitado em nenhuma posição')
print('os valores pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')
