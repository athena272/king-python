inicio = int(input('Digite o início da progressão: '))
razao = int(input('Digite o valor da razão, o valor de casas a serem puladas: '))
decimo_termo = inicio + (10 - 1) * razao
for i in range(inicio, decimo_termo, razao):
    print('{}'.format(i), end= ' -> ')
print(' THE END')