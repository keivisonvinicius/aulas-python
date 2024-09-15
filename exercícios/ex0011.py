largura = float(input('qual a largura da parede? '))
altura = float(input('qual a altura da parede? '))
area = altura * largura
litro = area/2
print('sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('para pintar essa parede você precisará de {:.2f} litros de tinta'.format(litro))
