import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo nome: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1, n2, n3, n4]
ordem = random.shuffle(lista)
print('a ordem de apresentação do trabalho é {}'.format(lista))
