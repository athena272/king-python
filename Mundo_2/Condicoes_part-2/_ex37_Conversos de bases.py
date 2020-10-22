numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão:'
      '\n'
      '\n\033[30m[1] para transformar em Binário\033[m'
      '\n[2] para transformar em Octal'
      '\n\033[30m[3] para transformar em Hexadecimal'
      '\n')
opcao = int(input('\033[1;35mDigite aqui sua escolha: '))
if opcao == 1:
    print('\n'
          '{} convertido para Binário é \033[4;34m{}\033[m'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('\n'
          '{} convertido para Octal é \033[4;34m{}\033[m'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('\n'
          '{} convertido para Hexadecimal é \033[4;34m{}\033[m'.format(numero, hex(numero)[2:]))
else:
    print('\033[1;31mVocê escolheu uma opção inválida!!!')