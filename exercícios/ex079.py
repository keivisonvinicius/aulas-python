valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores: 
        valores.append(valor)
        print(f'valor adicionado com sucesso...') 
    else:
        print(f'Valor duplicado! Não vou adicionar...')
    resposta = str.upper(input('Deseja continuar?[S/N]: ')).strip()[0]
    if resposta == 'N':
        break
valores.sort()
print(f'Sua lista ficou assim: {valores}')
