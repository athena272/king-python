somar_par = 0
for i in (1, 7):
    num = int(input('Digite um número inteiro, por favor: '))
    if (num % 2 == 0):
        somar_par += num
print('O soma dos números pares desse laço é {}'.format(somar_par))