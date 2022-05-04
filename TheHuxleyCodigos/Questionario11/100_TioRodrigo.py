tamanho = int(input())
matriz = []
for caso in range(1,tamanho+1):
    linha = input().split()
    linha = [int(elem) for elem in linha]
    matriz.append(linha)

diagonal = []
diagonal.append([matriz[-linha-1][-linha-1] for linha in range(len(matriz))])

for i in range(len(matriz)):
    matriz[i][i] = diagonal[0][i]


for i in range(len(matriz)):
    matriz[len(matriz)-i-1][i] =  2*matriz[len(matriz)-1-i][i]

matrizTransp = []
for linha in range(len(matriz)):
    coluna = []
    for colum in  range(len(matriz)):
        coluna.append(matriz[colum][linha])
    matrizTransp.append(coluna)

def imprimirMatriz(m):
    for fila in m:
        fila = [str(elem) for elem in fila]
        print(" ".join(fila)+" ")
    print()

imprimirMatriz(matrizTransp)