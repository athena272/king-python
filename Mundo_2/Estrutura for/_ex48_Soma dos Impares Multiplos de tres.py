soma = 0
i_cont = 0
for i in range(1, 501, 2):
    if (i % 3 == 0):
        soma += i
        i_cont += 1
print('A soma de todos os {} números ímpares múltiplos entre 1 à 500 de "3" é igual a {}'.format(i_cont, soma))