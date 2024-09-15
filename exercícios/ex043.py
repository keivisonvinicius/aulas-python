peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do seu peso ideal')
elif 18.5 <= IMC < 25:
    print('Você está no seu peso ideal')
elif 25 <= IMC < 30:
    print('Você está em sobrepeso')
elif 30 <= IMC < 40:
    print('Você está em obesidade!')
elif IMC > 40:
    print('Você está em obesidade mórbida, cuidado!')