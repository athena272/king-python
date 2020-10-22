#numeros primos
cont = 0
num = int(input('Digite um número: '))
for i in range(1, (num+1)):
    if (num % i == 0):
        print('\033[1;34m{}\033[m'.format(i), end=' ')
        cont += 1
    else:
        print('\033[1;31m{}\033[m'.format(i), end=' ')
if (cont == 2):
    print('\n'
          'O número {} É primo, pois só foi possível dividílo {} vezes'.format(num, cont))
else:
    print('\n'
          'O número {} NÃO é primo, pois foi possível dividílo {} vezes'.format(num, cont))
