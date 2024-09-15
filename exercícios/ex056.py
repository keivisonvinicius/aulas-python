soma = 0
cont = 0
maioridadehomem = 0
nomevelho = ''
for i in range(1,5):
    print('-'*5, '{} PESSOA'.format(i), '-'*5)
    nome = str.upper(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    Sexo = str.upper(input('Sexo[M/F]: ')).strip()
    soma += idade
    if i == 1 and Sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if Sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    media = soma/4
    if Sexo == 'F':
        if idade < 20:
            cont += 1
print('A média de idade do grupo foi de {} anos'.format(media))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
