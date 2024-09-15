#com a formula matematica
'''import math
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjascente = float(input('Comprimento do cateto adjascente: '))
hipotenusa = (cateto_adjascente ** 2 + cateto_oposto ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))'''

#com modulos
from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente: '))
hip = hypot(co,ca)
print('a hipotenusa mede {}'.format(hip))
