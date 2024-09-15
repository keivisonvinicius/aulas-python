soma = 0
cont = 0
for i in range(1,7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números pares e a soma deles foi {}'.format(cont, soma))