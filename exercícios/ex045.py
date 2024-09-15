import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = (random.randint(0,2))
print('''Suas opções: 
(0) PEDRA
(1) PAPEL
(2) TESOURA''')
jogador = int(input('sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('='*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('='*20)
if computador == 0:
    if jogador == 0:#pedra
        print('EMPATE')
    elif jogador == 1:
        print('VITÓRIA DO JOGADOR')
    else:
        print('VITÓRIA DO COMPUTADOR')

elif computador == 1:#papel
    if jogador == 0:
        print('VITÓRIA DO COMPUTADOR')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('VITÓRIA DO JOGADOR')

elif computador == 2:#tesoura
    if jogador == 0:
        print('VITÓRIA DO JOGADOR')
    elif jogador == 1:
        print('VITÓRIA DO COMPUTADOR')
    else:
        print('EMPATE')


