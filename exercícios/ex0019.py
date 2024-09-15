from random import choice
A1 = str(input('primeiro aluno: '))
A2 = str(input('segundo aluno: '))
A3 = str(input('terceiro aluno: '))
A4 = str(input('quarto aluno: '))
lista = [A1, A2, A3, A4]
escolha = choice(lista)
print('o aluno escolhido foi: {}'.format(escolha))
