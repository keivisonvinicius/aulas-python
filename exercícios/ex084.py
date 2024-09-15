galera = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('NOME: ')))
    dados.append(float(input('PESO: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]

    galera.append(dados[:])
    dados.clear()
    resposta = str.lower(input('Quer continuar?[S/N]: ')).strip()[0]
    if resposta == 'n':
        break
print(f'Ao todo você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {mai}kg.Peso de',end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {men}kg.Peso de',end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]')

