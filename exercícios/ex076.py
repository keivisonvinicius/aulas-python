listagem = ('lapis', 1.75,
            'caneta', 1.95,
            'caderno', 22.50,
            'mochila', 175.99,
            'borracha', 2)
print('-='*30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-='*30)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2F}')