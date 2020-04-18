#sequencia Fibonati
# 0 - 1 - 1 - 2 -3 - 5 - 8 -13
# pos1 pos2
print('\033[1;36m-=\033[m' * 20)
print('\033[33mSequência de Fibonacci\033[m')
print('\033[1;36m-=\033[m' * 20)
num = int(input('Quantos termos da sequência você quer exibir: '))
pos_1 = 0
pos_2 = 1
print('\033[1;35m-' * 20)
print('{} → {}'.format(pos_1, pos_2), end='')
cont = 3
while (cont <= num):
    pos_3 = pos_2 + pos_1
    print(' → {}'.format(pos_3), end='')
    pos_1 = pos_2
    pos_2 = pos_3
    cont += 1
print(' → THE END')