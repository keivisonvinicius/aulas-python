cidade = str.lower(input('Em que cidade você nasceu? ')).strip()
c = 'santo' in cidade.split()[0]
if(c == True):
    print('sua cidade começa com a palavra santo')
else:
    print('sua cidade não começa com a palavra santo')
