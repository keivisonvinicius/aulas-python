print('Gerador de PA')
print('=*='*10)
p1 = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO DA PA: '))
termo = p1
cont = 1
while cont <= 10 :
    print('{} ->'.format(termo), end=' ')
    termo += razao
    cont+=1
print('FIM')
