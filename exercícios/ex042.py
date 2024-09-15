r1 = float(input('comprimento da primeira reta: '))
r2 = float(input('comprimento da segunda reta: '))
r3 = float(input('comprimento da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possivel FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Não é possivel formar um triângulo!')




