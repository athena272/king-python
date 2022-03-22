listaValores = input().split()

limiteInferior = int(listaValores[0])
limiteSuperior = int(listaValores[1])

ano = limiteInferior
qtdAnosBissexto = 0
while ano <= limiteSuperior:
    if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        print(ano)
        qtdAnosBissexto = 1
    ano += 1

if(qtdAnosBissexto == 0):
    print("-1")