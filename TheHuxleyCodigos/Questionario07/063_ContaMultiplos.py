valor1 = int(input())
valor2 = int(input())

cont = 1
qtdMultiplos = 0
while cont < 50:
    multValor1 = (cont % valor1 == 0)
    multValor2 = (cont % valor2 == 0)
    if(multValor1 and multValor2):
        qtdMultiplos += 1

    cont += 1

print(qtdMultiplos)