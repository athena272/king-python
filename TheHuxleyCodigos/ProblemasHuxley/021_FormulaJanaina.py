limiteInferior = int(input())
limiteSuperior = int(input())

cont = limiteInferior
while cont <= limiteSuperior:
    calculo =  (cont ** 2) - (4 * cont) + 5
    print(calculo)

    cont += 1