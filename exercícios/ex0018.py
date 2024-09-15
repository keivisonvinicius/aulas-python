import math
angulo = int(input('Valor do ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(sen, cos, tg))

