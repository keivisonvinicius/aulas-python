'''primeiro_valor = float(input('Qual o peso da 1ª pessoa: ')) #uma forma de fazer
maximo = primeiro_valor
minimo = primeiro_valor'''
maximo = 0
minimo = 0
for i in range(1,6):
    peso = float(input('Qual o peso da {}ª  pessoa: '.format(i)))
    if i == 1:    #definindo o primeiro termo como o maior e o menor
        maximo = peso
        minimo = peso
    else:     #testando os proximos termos se sao maiores ou menores que o primeiro
        if peso > maximo:
            maximo = peso
        elif peso < minimo:
            minimo = peso
print('O maior peso lido foi de {}kg'.format(maximo))
print('O menor peso lido foi de {}kg'.format(minimo))


