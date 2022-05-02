def somasSucessivas(limiteSuperior,limiteInferior):
    if limiteInferior == 0: 
        return 0
    elif limiteInferior == 1:
        return limiteSuperior
    elif limiteInferior < 0:
        return -somasSucessivas(limiteSuperior,-limiteInferior)
    else:
        return limiteSuperior + somasSucessivas(limiteSuperior, limiteInferior-1)

limiteSuperior = int(input())
limiteInferior = int(input())

print(somasSucessivas(limiteSuperior,limiteInferior))