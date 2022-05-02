def somaAcima(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i:
                soma += matriz[i][j] 
    
    return soma

def somaAbaixo(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j < i:
                soma += matriz[i][j] 
    
    return soma


posicao = input()
limiar = int(input())
grandezaMatriz = int(input())
matrizQuestao = []
for _ in range(grandezaMatriz):
    fila = input().split()
    matrizQuestao.append( [int(elem) for elem in fila] )

saidaSoma = somaAcima(matrizQuestao)
if (posicao == 'abaixo'):
    saidaSoma = somaAbaixo(matrizQuestao)


serMaior = False if saidaSoma < limiar else  True
print(serMaior)