matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPar = somaTer = Maior = 0
for l in range(0, 3): #for's de alimentação
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
print('-='*30)
for l in range(0, 3): #for's para mostrar a matriz estruturada
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos números pares digitados é: {somaPar}')
for l in range(0, 3):
    somaTer += matriz[l][2]
print(f'A soma dos números da terceira coluna é: {somaTer}')
for c in range(0, 3):
    if c == 0:
        Maior = matriz[1][0]
    elif matriz[1][c] > Maior:
        Maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {Maior}')



