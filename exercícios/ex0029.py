vel = float(input('Qual a velocidade do carro?(KM/H) '))
limite = 80
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado em R${:.1f} '.format(multa))

print('Tenha um bom dia! diriga com segurança')
