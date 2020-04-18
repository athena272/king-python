tabu_use = int(input('Digite um número para criarmos a tabuada dele: '))
for i in range(0, 11):
    multiplicar = i * tabu_use
    print('{} X {} = {}'.format(i, tabu_use, multiplicar))