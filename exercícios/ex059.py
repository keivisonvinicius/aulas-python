escolha = 0
n1 = int(input('PRIMEIRO NÚMERO: '))
n2 = int(input('SEGUNDO NÚMERO: '))
while escolha != 5:
    print('''ESCOLHA A OPERAÇÃO:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    escolha = int(input('>>>>>Sua escolha: '))
    if escolha == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}'.format(n1, n2, soma))
    elif escolha == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicacao))
    elif escolha == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        elif n2 > n1:
            print('O maior número é {}'.format(n2))
        else:
            print('Não há número maior, pois os dois são iguais')
    elif escolha == 4:
        print('Iforme os números novamente')
        n1 = int(input('PRIMEIRO NÚMERO: '))
        n2 = int(input('SEGUNDO NÚMERO: '))
    elif escolha == 5:
        print('Fim')
    else:
        print('Opção inválida, tente novamente')
    print('=*='*10)
