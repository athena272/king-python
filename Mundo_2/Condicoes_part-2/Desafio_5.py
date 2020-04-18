nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
somar= (nota1 + nota2) / 2
print('|Tabelinha da escola|'
      '\n|Média < 5 --- \033[1;31mREPROVADO\033[m|'
      '\n|Média entre 5 e 6.9 --- \033[1;33mRECUPERAÇÃO\033[m|'
      '\n|Média >= 7 --- \033[1;32mAPROVADO\033[m|'
      '\n')
print('Sua média foi \033[1;30m{}'.format(somar))
if somar < 5.0:
    print('\n'
          '\033[1;31mVocê está REPROVADO!!! Lamento...')
elif (somar > 5.0) and (somar <= 6.9):
    print('\n'
          '\033[1;33mVocê está na RECUPERAÇÃO!!! Estude mais, sei que tu consegues...')
else:
    print('\n'
          '\033[1;32mVocê está APROVADO!!! Parabéns, descanse e continue assim...')