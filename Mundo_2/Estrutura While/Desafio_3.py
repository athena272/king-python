from time import sleep
valor_1= int(input('Digite o primeiro valor: '))
valor_2= int(input('Digite o segundo valor: '))
escolha = 0
while (escolha != 5):
    print('\n'
         '[1] para somar'
         '\n[2] para multiplicar'
         '\n[3] para saber maior número'
        '\n[4] novos números'
        '\n[5] sair do programa'
          '\n')
    escolha = int(input('O que você deseja fazer: '))
    if (escolha == 1):
        somar = valor_1 + valor_2
        print('\033[36m-=\033[m' * 20)
        print('A soma dos valores {} + {} = {} '.format(valor_1, valor_2, somar))
        print('\033[36m-=\033[m' * 20)
    elif (escolha == 2):
        multi = valor_1 * valor_2
        print('\033[36m-=\033[m' * 20)
        print('A multiplicação entre {} X {} = {}'.format(valor_1, valor_2, multi))
        print('\033[36m-=\033[m' * 20)
    elif (escolha == 3):
        if (valor_1 > valor_2):
            print('\033[36m-=\033[m' * 20)
            print('{} > {}'.format(valor_1, valor_2))
            print('\033[36m-=\033[m' * 20)
        elif (valor_2 > valor_1):
            print('\033[36m-=\033[m' * 20)
            print('{} > {}'.format(valor_2, valor_1))
            print('\033[36m-=\033[m' * 20)
        else:
            print('\033[36m-=\033[m' * 20)
            print('{} == {}'.format(valor_1, valor_2))
            print('\033[36m-=\033[m' * 20)
    elif (escolha == 4):
        print('\033[1;31mInforme os números de novo!\033[m')
        valor_1 = int(input('Digite o primeiro valor: '))
        valor_2 = int(input('Digite o segundo valor: '))
    elif (escolha == 5):
        print('\033[36m-=\033[m' * 20)
        print('\033[33mFinalizando programa....\033[m'.center(50))
        print('\033[36m-=\033[m' * 20)
        sleep(1.2)
print('\n\033[32mPrograma FInalizado, volte sempre\033[m')