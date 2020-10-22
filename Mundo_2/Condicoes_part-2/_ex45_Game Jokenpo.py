from random import randint
from time import  sleep
opcao= ['TESOURA', 'PEDRA', 'PAPEL']
computador_choice = randint(0,2)
print('Suas escolhas são:'
      '\n\033[1;34m[0] para TESOURA\033[m'
      '\n\033[1;35m[1] para PEDRA\033[m'
      '\n\033[1;36m[2] para PAPEL\033[m'
      '\n')
adversario = int(input('Qual a sua escolha?: '))
if adversario > 2:
    print('\n\033[1;31mOpção INVÁLIDA\033[m')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(2)
    print('\033[1;34m-=' * 20)
    print('\033[1;33mO computador escolheu\033[m \033[4;30m{}\033[m'
          '\n\033[1;33mO jogador escolheu\033[m \033[4;30m{}\033[m'.format(opcao[computador_choice], opcao[adversario]))
    print('\033[1;34m-=' * 20)
    if (computador_choice == adversario):
        print('\n'
              '\033[4;33mEMPATE')
    elif (computador_choice ==0):
        if (adversario == 1):
            print('\n'
                  '\033[1;32mJOGADOR VENCE\033[m'
                  '\n\033[1;31mCOMPUTADOR PERDE\033[m')
        elif (adversario == 2):
            print('\n'
                  '\033[1;32mCOMPUTADOR VENCE\033[m'
                  '\n\033[1;31mJOGADOR PERDE\033[m')
    elif (computador_choice == 1):
        if (adversario == 0):
            print('\n'
                  '\033[1;32mCOMPUTADOR VENCE\033[m'
                  '\n\033[1;31mJOGADOR PERDE\033[m')
        elif (adversario == 2):
            print('\n'
                  '\033[1;32mJOGADOR VENCE\033[m'
                  '\n\033[1;31mCOMPUTADOR PERDE\033[m')
    elif (computador_choice == 2):
        if (adversario == 0):
            print('\n'
                  '\033[1;32mJOGADOR VENCE\033[m'
                  '\n\033[1;31mCOMPUTADOR PERDE\033[m')
        elif (adversario == 1):
            print('\n'
                  '\033[1;32mCOMPUTADOR VENCE\033[m'
                  '\n\033[1;31mJOGADOR PERDE\033[m')
    else:
        print('\n\033[1;31mOpção INVÁLIDA\033[m')