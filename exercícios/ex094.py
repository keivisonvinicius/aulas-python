pessoas = {}
lista = []
tot = 0
soma = 0
media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    tot += 1
    pessoas['sexo'] = str.upper(input('Sexo[M/F]:')).strip()[0]
    while pessoas['sexo'] not in 'mMfF':
            print('ERRO! Por favor digite apenas M ou F.')
            pessoas['sexo'] = str.lower(input('Sexo[M/F]:')).strip()[0]
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    media = soma / tot
    lista.append(pessoas.copy())
    resposta = str.upper(input('Quer continuar?[S/N]: '))[0]
    while resposta not in 'nNsS':
        print('ERRO! Por favor digite apenas sim ou não.')
        resposta = str.upper(input('Quer continuar?[S/N]: '))[0]
        if resposta == 'N':
            break
    if resposta== 'N':
         break
print(f'o grupo tem {tot} pessoas')
print(f'a média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram:',end='')
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]}')
print()
print(f'Lista das pessoas que estão acima da média: ')
for pessoa in lista:
     if pessoa['idade'] > media:
          print('     ',end='')
          for k,v in pessoa.items():
               print(f'{k} = {v};',end='')
          print()
print('<<<< ENCERRADO >>>>')

