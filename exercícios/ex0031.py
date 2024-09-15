dist = int(input('Qual a distância da viagem?: '))
if dist <= 200:
    preco = 0.50 * dist
    print('o valor da passagem é R${:.2f}'.format(preco))
else:
    preco = 0.45 * dist
    print('o valor da passagem é R${:.2f}'.format(preco))