def soVogal(textoRisada):
    status = True
    letraAnterior = textoRisada[0]
    for letra in textoRisada:
        if(letra not in 'aeiou' or letraAnterior != letra):
            status = False
            break
        letraAnterior = letra    
    return status

def soConsoante(textoRisada):
    status = True
    for letra in textoRisada:
        if(letra in 'aeiou'):
            status = False
            break
    return status

def risadaInvalida(textoRisada):
    status = False
    maior50Letras = len(textoRisada)
    if(maior50Letras > 50 or soConsoante(textoRisada)):
        status = True
    
    return status


def risadaEngracada(textoRisada):
    status = False
    textoEngracado = ('hahaha' in textoRisada or 'huaauhahhuahau' in textoRisada)
    textoSemGraca = ('riajkjdhhihhjak' in textoRisada or 'huehuehue' in textoRisada)
    terSoVogal = soVogal(textoRisada)
    
    if((textoEngracado or terSoVogal) and not(textoSemGraca)):
        status = True #Sem graca
    
    return status


qtdLeituras = int(input())

cont = 0
while cont < qtdLeituras:
    textoRisada = input().lower()
    statusRisada = 'SEM GRACA'
    if(risadaEngracada(textoRisada)):
        statusRisada = 'ENGRACADA'
    if(risadaInvalida(textoRisada)):
        statusRisada = 'INVALIDA'
    
    print(statusRisada)

    cont += 1