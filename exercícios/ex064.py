print('Gerador de PA')
print('=*='*10)
p1 = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO DA PA: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total :
        print('{} ->'.format(termo), end=' ')
        termo += razao
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('Progressão finalizada com {} termos mostrados'.format(total))