def matrizem3(matriz):
    matriz3x3 = []
    linha3x3 = []
    instance = True
    for linha in range(0,len(matriz),3):
        for linha2 in range(len(matriz)):
            linha3x3.append(matriz[linha2][linha:linha+3])
            if len(linha3x3) % 3 == 0:
                matriz3x3.append(linha3x3)
                linha3x3 = []
    for matriz in matriz3x3:
        ordenado = []
        for linha in matriz:
            for elem in linha:
                ordenado.append(elem)
                ordenado.sort()
     
        if ordenado != [1,2,3,4,5,6,7,8,9]:
            instance = False
    return instance
         


def linhaPorLinha(matriz):
    instance = True
    for linha in (matriz):
        linhaOrd = sorted(linha)
        if linhaOrd != [1,2,3,4,5,6,7,8,9]:
            instance = False
    return instance

def coluna_Coluna(matriz):
    instance = True
    for linha in range(len(matriz)):
        coluna = []
        for colun in matriz:
            coluna.append(colun[linha])
        coluna.sort()
        if coluna != [1,2,3,4,5,6,7,8,9]:
            instance = False
    return instance

def sudoku(matriz):
    return (coluna_Coluna(matriz) and linhaPorLinha(matriz) and matrizem3(matriz))    

repeticoes = int(input())
for caso in range(1,1+repeticoes):
    matriz = []
    for _ in range(9):
        linha = input().split()
        linha = [int(elem) for elem in linha]
        matriz.append(linha)
    print("Instancia",caso)
    if sudoku(matriz):
        print("SIM")
    else:
        print("NAO")
    print()