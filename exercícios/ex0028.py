import random
from time import sleep
num = random.randint(0,5)
print('-=-'*20)
print('pensei em um número entre 0 e 5, tente adivinhá-lo... ')
print('-=-'*20)
tent = int(input('em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if tent == num:
    print('PARABÉNS!, você conseguiu me vencer!')
else:
    print('GANHEI! eu pensei no número {}'.format(num))
