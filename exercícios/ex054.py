from datetime import date
a = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('em que ano a {} pessoa nasceu?: '.format(pess)))
    idade = a - nasc
    if idade >= 21:
        totmaior+= 1
    else:
        totmenor += 1
print('{} pessoas são maiores de idade e {} são menores de idade.'.format(totmaior,totmenor))