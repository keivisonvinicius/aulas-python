lista = list()
while True:
    valores = int(input('Digite um número: '))
    lista.append(valores)
    resposta = str.lower(input('Quer continuar?[S/N]: ')).strip()[0]
    if resposta == 'n':
        break
impares = list()
pares = list()
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'lista completa {lista}')
print(f'lista de números pares: {pares}')
print(f'lista de números ímpares: {impares}')
