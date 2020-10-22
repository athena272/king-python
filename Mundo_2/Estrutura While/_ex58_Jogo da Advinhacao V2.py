from random import randint
from time import sleep
computador_pensar = randint(0, 10)
print('\033[33mPensei em um número entre 0 e 10'
      '\nTente adivinha, se puder...\033[m'
      '\n')
escolha= int(input('Em que número acha que pensei: '))
if (escolha == computador_pensar):
    print('Processando...')
    sleep(1.5)
    print('\n'
          '\033[32mParabéns você advinhou, eu realmente pensei no número {}'.format(escolha))
else:
    print('Processando...')
    sleep(1.5)
    print('\n'
          
          '\033[1;31mBAAAAMMMMMMMMM'
          '\nVocê errou!!!'
          '\nHIHIHI\033[m')
    vezes = 1
    while (escolha != computador_pensar):
        escolha = int(input('Tente novamente, por favor: '))
        print('Processando...')
        sleep(1.5)
        if (escolha != computador_pensar):
            print('\n'
                  '\033[1;31mBAAAAMMMMMMMMM'
                  '\nVocê errou!!!'
                  '\nHIHIHI\033[m')
            vezes += 1
        else:
            print('\n'
            '\033[32mParabéns você advinhou, eu realmente pensei no número {}\033[m'
            '\n\033[1;33mMas voce precisou de {} tentativas para acertar!'.format(escolha, vezes))