txt = str.lower(input('Digite uma frase: ')).strip().replace(' ', '')
inverso = txt[::-1]
print('O inverso de {} é {}'.format(txt,inverso))
if txt == inverso:
    print('Temos um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
