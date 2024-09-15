from random import randint
cont = 0
while True:
    jogador = int(input('Diga um número: '))
    e = str.upper(input('PAR OU IMPAR?: ')).strip()[0]
    while e not in 'PI':
        e = str.upper(input('PAR OU IMPAR?: ')).strip()[0]
    computador = randint(0,10)
    resultado = jogador + computador
    if e == 'P':
        if resultado % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU PAR')
            print('-'*25)
            print('VOCÊ VENCEU')     
            cont += 1   
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU ÍMPAR')
            break
    if e == 'I':
        if resultado % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU PAR')
            break
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU ÍMPAR')
            print('-'*25)
            print('VOCÊ VENCEU')
            cont += 1
    print(f'Vamos jogar novamente...')
print(f'GAME OVER! VOCÊ VENCEU UM TOTAL DE {cont} vezes')