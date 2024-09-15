a = int(input('PRIMEIRO NÚMERO: '))
b = int(input('SEGUNDO NÚMERO: '))
maior = a
menor = a
if b < a:
    print('O PRIMEIRO valor é maior!')
elif b > a:
    print('O SEGUNDO valor é maior!')
else:
    print('os dois valores são IGUAIS!')