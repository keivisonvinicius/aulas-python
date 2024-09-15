casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$ '))
ano = int(input('Quantos anos de financiamento?  '))
prestacao = casa / (ano* 12 )
sal = salario * 30/100
if prestacao < sal:
    print('para pagar uma casa de R${} em {} anos a prestação será de {}'.format(casa, ano, prestacao))
    print('EMPRÉSTIMO APROVADO!')
else:
    print('para pagar uma casa de R${} em {} anos a prestação será de {}'.format(casa, ano, prestacao))
    print('EMPRÉSTIMO NEGADO!')