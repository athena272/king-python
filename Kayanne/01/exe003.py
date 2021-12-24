print('\n'
         '[1] para somar (+)'
         '\n[2] para subtrair (-)'
         '\n[3] para multiplicar (x)'
        '\n[4] para dividir (/)'
        '\n')

escolha = int(input('O que você deseja fazer: '))

if escolha > 4 and escolha < 1:    
    print('OPÇÃO INVÁLIDA!!!')

else:
    valor1= int(input('\nDigite o primeiro valor: '))
    valor2= int(input('Digite o segundo valor: '))

    if escolha == 1: #soma

        soma = valor1 + valor2
        print(f'\nA soma resulta em {valor1} + {valor2} = {soma}')

    elif escolha == 2: #subtração

        subtrai = valor1 - valor2
        print(f'\nA subtração resulta em {valor1} - {valor2} = {subtrai}')

    elif escolha == 3: #multiplicação
        
        mult = valor1 * valor2
        print(f'\nA multiplicação resulta em {valor1} x {valor2} = {mult}')

    elif escolha == 4: #divisão

        division = valor1 / valor2
        print(f'\nA divisão resulta em {valor1} / {valor2} = {division}')

        

