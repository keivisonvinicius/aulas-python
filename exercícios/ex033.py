a = int(input('primeiro número: '))
b = int(input('segundo número: '))
c = int(input('terceiro número: '))
menor = a
maior = a
# verificando quem é menor
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
# verificando quem é maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('{}{}{} é o menor número'.format('\033[31m',menor,'\033[m'))
print('{}{}{} é o maior número'.format('\033[36m',maior,'\033[m'))