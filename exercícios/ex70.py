soma = mais1000 = maisbarato = cont =0
barato = ' '
while True:
    nome = str(input('NOME DO PRODUTO: '))
    valor = float(input('VALOR DA COMPRA: R$'))
    cont += 1
    soma += valor
    if valor > 1000:
         mais1000 += 1
    if cont == 1:
           maisbarato = valor
           barato = nome
    else:
        if valor < maisbarato:
             barato = nome
             maisbarato = valor
    r = ' '
    while r not in 'SN':
          r = str.upper(input('DESEJA ADICIONAR MAIS COMPRAS?[S/N]: ')).strip()[0]
    if r == 'N':
         break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${soma}')
print(f'Temos {mais1000} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${maisbarato:.2f}')
