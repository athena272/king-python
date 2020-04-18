from random import randint
from time import sleep
choices= ['PAPEL', 'PEDRA', 'TESOURA']
computador = randint(0,2)
print('Suas escolhas são:'
      '\n\033[1;34m[0] para TESOURA\033[m'
      '\n\033[1;35m[1] para PEDRA\033[m'
      '\n\033[1;36m[2] para PAPEL\033[m'
      '\n')
continuar = 's'
while (continuar == 's'):
    choice_player= int(input('Qual a sua escolha: '))
    if choice_player > 2:
        print('\n\033[1;31mOpção INVÁLIDA\033[m')
    else:
        if choice_player == 0:
            computador = 2
        elif choice_player == 1:
            computador = 0
        elif choice_player == 2:
            computador = 1
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        sleep(1.5)
        print('\033[1;34m-=' * 20)
        print('\033[1;33mO computador escolheu\033[m \033[4;30m{}\033[m'
              '\n\033[1;33mO jogador escolheu\033[m \033[4;30m{}\033[m'.format(choices[computador], choices[choice_player]))
        print('\033[1;34m-=' * 20)
        print('\n'
              '\033[1;32mCOMPUTADOR VENCE\033[m'
              '\n\033[1;31mJOGADOR PERDE\033[m')
        continuar= str(input('Deseja jogar novamente?: ')).lower().strip()[0]
        if (continuar == 'n'):
            break