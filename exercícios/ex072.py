numeros = ('zero', 'um', 'dois', 'três', 'quatro' , 
           'cinco', 'seis', 'sete', 'oito', 'nove', 
           'dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 
           'dezesseis','dezessete','dezoito','dezenove','vinte')
resposta = 's'
while resposta == 's':
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
    print(f'Você digitou o número {numeros[num]}')
    resposta = str.lower(input('Deseja digitar outro número?(S/N): ')).strip()[0]

    