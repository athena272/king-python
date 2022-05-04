dados_1 = [int(elem) for elem in input().split()]
linhas_1, colunas_1, imagem_1, imagem_2 = dados_1[0], dados_1[1], [], []
contador = 0

for _ in range(linhas_1):
    matriz = [int(elem) for elem in input().split()]
    imagem_1.append(matriz)

dados_2 = [int(elem) for elem in input().split()]
linhas_2, colunas_2 = dados_2[0], dados_2[1]

for _ in range(linhas_2):
    matriz = [int(elem) for elem in input().split()]
    imagem_2.append(matriz)


def saoiguais(m1, m2, i, j):
    for k in range(len(m2)):
        for l in range(len(m2[0])):
            if m2[k][l] != m1[k+i][l+j]:
                return False
    return True


for i in range(0, len(imagem_1) - len(imagem_2) + 1):
    for j in range(len(imagem_1[0]) - len(imagem_2[0]) + 1):
        if saoiguais(imagem_1, imagem_2, i, j):
            contador += 1

print(contador)
