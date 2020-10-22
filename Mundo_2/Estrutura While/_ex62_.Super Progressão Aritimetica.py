inicio = int(input('Digite o início da progressão: '))
razao = int(input('Digite o valor da razão, o valor de casas a serem puladas: '))
contador = 1
termos = 10
total = 0
while (termos != 0):
    total += termos
    while (contador <= total):
        if (contador == 1):
            print('{}'.format(inicio), end=' -> ')
        else:
            inicio += razao
            print('{}'.format(inicio), end=' -> ')
        contador += 1
    print('PAUSA')
    termos = int(input('Mais quantos termos você quer mostrar: '))
print('\nTHE END'
      '\nForam exibidos {} termos'.format(total))