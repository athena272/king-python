print('\033[1;36m-_\033[m' * 30, end='')
print('\nJogo PAR ou ÍMPAR')
print('\033[1;36m-_\033[m' * 30, end=''
      '\n')
from random import randint
vitorias = 0
while True:
    computador_escolha = randint(0, 10)
    jogador_choice = int(input('Digite um valor: '))
    par_inpar = str(input('Par ou Ímpar? [p / i]: ')).strip().lower()[0]
    soma = jogador_choice + computador_escolha
    print('\033[1;34m--\033[m' * 20, end=''
          '\n')
    print(f'Você jogou {jogador_choice} e o Computador {computador_escolha}. Logo a soma é {soma}')
    print('\033[1;34m--\033[m' * 20, end=''
          '\n')
    if (par_inpar == 'p') and (soma % 2 == 0):
        print('\033[32mVOCÊ GANHOU\033[m'
              '\nVamos Jogar novamente...')
        print('-=' * 20)
        vitorias += 1
    elif (par_inpar == 'i') and (soma % 2 != 0):
        print('\033[32mVOCÊ GANHOU\033[m'
              '\nVamos Jogar novamente...')
        print('-=' * 20)
        vitorias += 1
    else:
        print('\033[1;31mBAAAAMMMMMM!!! VOCÊ PERDEU!!!\033[m')
        print(f'\033[1;31mGAME OVER!\033[m \033[32mVocê ganhou {vitorias} vez(es)\033[m')
        break


