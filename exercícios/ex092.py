from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['Carteira'] = int(input('Carteira de trabalho(0 não tem): '))
if dados['Carteira'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário:R$'))
    aposentadoria = dados['ano de contratação'] + 35
    dados['aposentadoria'] = aposentadoria - datetime.now().year + dados['idade']
print('-='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
