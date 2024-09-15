n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))
m = (n1 + n2) / 2
if m < 5:
    print('ALUNO \033[31mREPROVADO\033[m com média {:.1f}'.format(m))
elif m >= 5 and m < 7:
    print('ALUNO EM \033[33mRECUPERAÇÃO\033[m com média {:.1f}'.format(m))
else:
    print('ALUNO \033[36mAPROVADO\033[m com média {:.1f}'.format(m))
