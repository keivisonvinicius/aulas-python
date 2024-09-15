from random import randint
maior = menor = 0
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), 
     randint(1,10), )
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}',end=' ')
print(f'\no maior valor foi {max(numeros)}')
print(f'o menor valor foi {min(numeros)}')