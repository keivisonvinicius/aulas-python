aluno = {}
aluno['nome'] = str(input('NOME: '))
aluno['media'] = float(input(f'média de {aluno["nome"]}: ' ))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno ['media'] < 7 and aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
elif aluno['media'] <=3:
    aluno['situação'] = 'Reprovado'

for k,v in aluno.items():
    print(f'{k} = {v}')