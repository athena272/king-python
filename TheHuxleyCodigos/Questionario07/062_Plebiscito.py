def haverFogos(qtdSim, qtdNao):
    queimaFogos = 'COM FOGOS'
    if(qtdSim <= qtdNao):
        queimaFogos = 'SEM FOGOS'
    
    return queimaFogos


qtdSim = 0
qtdNao = 0
while True:
    voto = input()
    if(voto.lower().strip()[0] == 'e'):
        break
    if(voto.lower().strip()[0] == 's'):
        qtdSim += 1
    elif(voto.lower().strip()[0] == 'n'):
        qtdNao += 1

resultado = haverFogos(qtdSim, qtdNao)
print(resultado)