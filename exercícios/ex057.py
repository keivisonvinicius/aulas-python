sexo = str.upper(input('Qual o seu sexo?[M/F]: ')).strip()
while sexo != 'M' and sexo != 'F':
    print('Resposta inválida. Por favor, informe seu sexo')
    sexo = str.upper(input('Qual o seu sexo?[M/F]: ')).strip()
print('sexo {} registrado com sucesso'.format(sexo))