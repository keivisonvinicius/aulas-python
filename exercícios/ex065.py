resposta = str.lower('Sim')
soma = 0
cont = 0
while resposta == 'sim':
    num = int(input('Digite um número: '))
    maior = num
    menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resposta = str.lower(input('Deseja continuar? '))
    cont += 1
    soma += num
    media = soma / cont
print('A média dos números é {:.2f}, o maior número digitado foi {} e o menor {}'.format(media, maior, menor))
