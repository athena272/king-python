def multMatriz(matrizA, matrizB):
    numLinhasA = len(matrizA)
    numColunasA = len(matrizA[0])
    numLinhasB = len(matrizB)
    numColunasB = len(matrizB[0])

    matrizMult = list()
    for linha in range(numLinhasA):
        matrizMult.append([])
        for coluna in range(numColunasB):
            matrizMult[linha].append(0)
            for k in range(numColunasA):
                matrizMult[linha][coluna] += matrizA[linha][k] * matrizB[k][coluna]
    
    return matrizMult


def imprimirMatriz(m):
     for fila in m:
        texto = ''
        for elem in fila:
             texto += str(elem) + " "
        textoSaida = " ".join(texto.split())
        print(textoSaida)
        

dadosMatriz = input().split()
qtdLinhasA = int(dadosMatriz[0])
qtdColumALinhaB = int(dadosMatriz[1])
qtdColumB = int(dadosMatriz[2])

matrizA = list()
for _ in range(qtdLinhasA):
    fila = input().split()
    matrizA.append( [int(elem) for elem in fila] )

matrizB = list()
for _ in range(qtdColumALinhaB):
    fila = input().split()
    matrizB.append( [int(elem) for elem in fila] )

matrizSaida = multMatriz(matrizA, matrizB)
imprimirMatriz(matrizSaida)