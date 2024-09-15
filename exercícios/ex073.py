tabela = ('palmeiras', 'grêmio', 'atlético mineiro', 'flamengo', 
          'botafogo', 'bragantino', 'fluminense', 'athlético-pr', 
          'internacional', 'fortaleza', 'são paulo', 'cuiabá', 'corinthians', 
          'cruzeiro', 'vasco', 'bahia', 'santos', 'goias', 'coritiba', 'américa-mg')
print('-='*45)
print(f'Os 5 primeiros colocados do brasileirão 2024 foram {tabela[:5]}')
print('-='*45)
print(f'Os times rebaixados foram {tabela[-4:]}')
print('-='*45)
print(f'A ordem alfabética da tabela é: {sorted(tabela)}')
print('-='*45)
print(f'O vasco está na {tabela.index("vasco") + 1} posição') 