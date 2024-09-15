jogador = {}
lista = []
jogador['nome'] = str(input('Nome do jogador: '))
jogador['gols'] = lista
partidas = int(input(f'Quantas partidade {jogador["nome"]} jogou? '))
jogador['total'] = 0
for i in range(partidas):
    gols = int(input(f'Quantos gols na partida {i + 1}? '))
    jogador['total'] += gols
    lista.append(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas ')
for i,v in enumerate(jogador['gols']):
    print(f' >Na partida {i + 1} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')