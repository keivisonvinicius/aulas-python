print('='*15)
print('LOJAS KEIVISON')
print('='*15)
valor = float(input('Qual o valor das compras?R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
forma = int(input('Qual é a opção? '))
if forma == 1:
     v = valor - (valor * 10/100)
     print('Sua compra de R${} vai custar R${} no final'.format(valor, v))
elif forma == 2:
     v = valor - (valor * 5/100)
     print('Sua compra de R${} vai custar R${} no final'.format(valor, v))
elif forma == 3:
    v = valor
    parcelas = valor/2
    print('Sua compra será parcelada em 2x de {}'.format(parcelas))
    print('Sua compra de R${} vai custar R${} no final'.format(valor, v))
elif forma == 4:
        parcelas = int(input('Quantas parcelas? '))
        p = (valor + (valor * 20/100)) / parcelas
        v = (valor + (valor * 20/100))
        print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(parcelas, p))
        print('Sua compra de R${} vai custar R${} no final'.format(valor, v))
else:
    print('\033[31mOpção inválida, tente novamente\033[m')
