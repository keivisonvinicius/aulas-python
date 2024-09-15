num = int(input('Digite um número: '))
soma = num
cont = 0
while num != 999:
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
print('foram digitados {} números e a soma entre eles é de {}'.format(cont, soma - 999))