listaTermos = input().split()

termoGrau2 = float(listaTermos[0])
termoGrau1 = float(listaTermos[1])
termoGrau0 = float(listaTermos[2])

def calcDelta(termo2, termo1, termo0):
    #errei o calculo do delta, elevei o termo de Grau 1 a (1/2)
    delta = ((termo1 ** 2) - 4 * termo2 * termo0)
    return delta

def raizPositiva(termo1, delta, termo2):
    #Esqueci de tirar a raiz de delta aqui
    #Esqueci de colocar o denominador 2*a entre parenteses, sem eles da erro devido a ordem de precedencia
    raiz1 = ((-1 * termo1) + (delta ** (1/2))) / (2 * termo2)
    return raiz1

def raizNegativa(termo1, delta, termo2):
    #Esqueci de tirar a raiz de delta aqui
    #Esqueci de colocar o denominador 2*a entre parenteses, sem eles da erro devido a ordem de precedencia
    raiz2 = ((-1 * termo1) - (delta ** (1/2))) / (2 * termo2)
    return raiz2

if(termoGrau2 == 0 or calcDelta(termoGrau2, termoGrau1, termoGrau0) < 0):
    print('Impossivel calcular')

else:
    oDelta = calcDelta(termoGrau2, termoGrau1, termoGrau0)
    raizLinha1 = raizPositiva(termoGrau1, oDelta, termoGrau2)
    raizLinha2 = raizNegativa(termoGrau1, oDelta, termoGrau2)

    print('R1 = %.5f' %raizLinha1)
    print('R2 = %.5f' %raizLinha2)


