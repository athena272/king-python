print('-=' * 25)
print('{:^30}'.format('BANCO O coisa'))
print('\033[32mTemos notas de R$50 ; R$20 ; R$10 e R$1\033[m')
print('-=' * 25)
quantia = int(input('Digite aqui um valor: R$'))
print('--' * 25)
retirando_quantia = quantia
dinheiro = 50
numero_dinheiro = 0
while True:
    if (retirando_quantia >= dinheiro):
        retirando_quantia -= dinheiro
        numero_dinheiro += 1
    else:
        if (numero_dinheiro > 0):
            print(f'Serão {numero_dinheiro} cédulas de R${dinheiro}')
        if (dinheiro == 50):
            dinheiro = 20
        elif (dinheiro == 20):
            dinheiro = 10
        elif (dinheiro == 10):
            dinheiro = 1
        numero_dinheiro = 0
        if (retirando_quantia == 0):
            break