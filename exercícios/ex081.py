lista = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resposta = str.lower(input('Deseja continuar?[S/N]: ')).strip()[0]
    if resposta == 'n':
        break
lista.sort(reverse=True)
print(f'foram digitados ao todo {len(lista)} números')
print(f'A lista, em forma decrescente, é: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
