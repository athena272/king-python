inicio = int(input('Digite o início da progressão: '))
razao = int(input('Digite o valor da razão, o valor de casas a serem puladas: '))
decimo = 1
while (decimo <= 10):
    if (decimo == 1):
        print('{}'.format(inicio), end=' -> ')
    else:
        inicio += razao
        print('{}'.format(inicio), end=' -> ')
    decimo += 1
print('THE END')