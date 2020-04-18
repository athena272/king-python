from datetime import date
print('\033[1;36m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m'
      '\n\033[1;33mPrograma da Confederação Nacional de Natação\033[m'
      '\n\033[1;36m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
nascimento = int(input('Qual a sua data de nascimento, por favor:\033[m '))
data_atual = date.today()
idade = data_atual.year - nascimento
print('\nSua idade atual é de {} anos'.format(idade))
if idade <= 9:
    print('\n'
          'Sua categoria é: \033[4;30mMIRIM')
elif (idade > 9) and (idade <= 14):
    print('\n'
          'Sua categoria é: \033[4;30mINFANTIL')
elif (idade > 14) and (idade <= 19):
    print('\n'
          'Sua categoria é: \033[4;30mJUNIOR')
elif (idade > 19) and (idade <= 20):
    print('\n'
          'Sua categoria é: \033[4;30mSÊNIOR')
elif (idade > 20):
    print('\n'
          'Sua categoria é: \033[4;30mMASTER')