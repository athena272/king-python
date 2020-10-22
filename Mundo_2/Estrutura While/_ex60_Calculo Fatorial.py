#fatorial de um número
factorial = 1
num = int(input('Digite um número: '))
print('Calculo do {}!'.format(num))
while (num > 0):
    print('{}'.format(num), end='')
    print(' X ' if num > 1 else ' = ', end='')
    factorial *= num
    num -=1
print('{}'.format(factorial), end='')

