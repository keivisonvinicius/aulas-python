maior18 = 0
homens = 0
mulheres20 = 0
while True:
    idade = int(input('IDADE: '))
    if idade > 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str.upper(input('SEXO[M/F]: ')).strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta  = str.upper(input('QUER CONTINUAR?[S/N]: ')).strip()[0]
    if resposta == 'N':
        break  
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres20} mulheres com menos de 20 anos')


    