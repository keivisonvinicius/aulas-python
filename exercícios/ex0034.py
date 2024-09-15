sal = float(input('qual o salário do funcionário?R$'))
if sal > 1250:
    aumento = sal + (sal * 10) / 100

else:
    aumento = sal + (sal * 15 / 100)
print('quem recebia R${:.2f}, passa a receber R${:.2f}'.format(sal, aumento))
