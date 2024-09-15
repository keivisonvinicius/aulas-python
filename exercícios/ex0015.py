dias = int(input('quantos dias alugados? '))
km = float(input('quantos KM rodados? '))
total = (dias * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(total))
