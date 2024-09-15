valores = list()
maior = menor = 0

for i in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {i}: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')

for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()

print(f'o menor valor digitado foi {menor} nas posições', end=' ')

for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')
 
