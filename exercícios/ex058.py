from random import randint
computador = randint(0,10)
print('='*55)
print('Pensei em um número entre 0 e 10, tente adivinhá-lo')
print('='*55)
cont = 0
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite?: '))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... tente novamente')
        if jogador < computador:
            print('Mais... tente novamente')
print('Você acertou!!! foram necessárias {} tentativas'.format(cont))