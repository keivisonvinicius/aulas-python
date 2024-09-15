import datetime
a = datetime.date.today().year
ano = int(input('ANO DE NASCIMENTO: '))
idade = a - ano
print('O atleta tem {} anos'.format(idade))
if idade <=9:
    print('CLASSIFICAÇÃO: mirim!')
elif idade <= 14:
    print('CLASSIFICAÇÃO: infantil')
elif idade <= 19:
    print('CLASSIFICAÇÃO: junior')
elif idade <=25:
    print('CLASIFICAÇÃO: sênior')
else:
    print('CLASSIFICAÇÃO: master')