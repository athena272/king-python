def removeRepetidos(listaNum):
    listaSemRepetidos = list()
    for elem in listaNum:
        if elem not in listaSemRepetidos:
            listaSemRepetidos.append(elem)
    
    return listaSemRepetidos


qtdLeituras = int(input())
figurinhasJoao = list()
figurinhasMaria = list()
for i in range(qtdLeituras):
    numSerie = int(input())
    if(numSerie % 2 == 0):
        figurinhasJoao.append(numSerie)
    else:
        figurinhasMaria.append(numSerie)
    
qtdSerieJoao = len(figurinhasJoao)
qtdSerieMaria = len(figurinhasMaria)

figurinhasJoao = removeRepetidos(figurinhasJoao)
figurinhasMaria = removeRepetidos(figurinhasMaria)
pontosVencedor = max(sum(figurinhasMaria), sum(figurinhasJoao))

print(qtdSerieJoao)
print(qtdSerieMaria)
print(pontosVencedor)