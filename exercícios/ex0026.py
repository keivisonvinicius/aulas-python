frase = str.upper(input('Escreva uma frase qualquer: ')).strip()
print('A letra "A" aparece {} vez(es) na frase'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))