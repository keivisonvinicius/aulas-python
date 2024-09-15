import datetime
ano = int(input('Em que ano você nasceu? '))
a = datetime.date.today().year
idade = a - ano
print('Quem nasceu em {} tem {} anos em 2023.'.format(ano,idade))
if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    falta = 18 - idade
    if falta == 1:
        print('Ainda falta {} ano para o alistamento'.format(falta))
    else:
        print('Ainda faltam {} anos para o alistamento'.format(falta))
    print('Seu alistamento será em {}'.format(a + falta))
else:
    passou = idade - 18
    if passou == 1:
        print('você ja deveria ter se alistado a {} ano'.format(passou))
    else:
        print('você ja deveria ter se alistado a {} anos'.format(passou))
    print('seu alistamento foi em {}'.format(a - passou))

