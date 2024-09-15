from datetime import date
ano = int(input('Que ano você quer analisar? COLOQUE 0 PARA ANALISAR O ANO ATUAL '))
if ano == 0:
    ano = date.today().year #pega a data atual, mais especificamente o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))