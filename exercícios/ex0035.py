r1 = float(input('comprimento da primeira reta: '))
r2 = float(input('comprimento da segunda reta: '))
r3 = float(input('comprimento da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('é possivel formar um triângulo')
else:
    print('não é possível formar um triângulo')