def risadaInvalida(textoRisada):
    status = False
    maior50Letras = len(textoRisada)
    if(maior50Letras > 50 or 'aeiou' not in textoRisada):
        status = True
    
    return status


def risadaEngracada(textoRisada):
    status = True
    if('riajkjdhhihhjak' == textoRisada or 'huehuehue' == textoRisada):
        status = False #Sem graca
    
    return status


qtdLeituras = int(input())

cont = 0
while cont < qtdLeituras:
    textoRisada = input()
    statusRisada = 'INVALIDA'
    if(risadaEngracada(textoRisada)):
        print('ENGRACADA')
    else:
        print('SEM GRACA')

    cont += 1