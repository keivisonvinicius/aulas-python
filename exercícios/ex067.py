while True:
    print(f'='*35)
    tb = int(input('Quer ver a tabuada de qual valor? '))
    if tb < 0:
        break
    n = 0
    while n < 11:
       print(f'{tb} x {n}  = {tb * n}')
       n += 1
print(f'encerrando programa...')
    