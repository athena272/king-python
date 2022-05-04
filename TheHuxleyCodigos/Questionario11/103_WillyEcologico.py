def contar(array, altura):
    soma = 0
    for i in array:
        if i > altura:
            soma += i - altura
    return soma


def buscabinaria(array, i, j, m, menor=0):
    if i <= j:
        media = int(i + (j - i) / 2)

        if contar(array, array[media]) == m:
            return media
        elif contar(array, array[media]) > m:
            return buscabinaria(array, media + 1, j, m, media)
        else:
            return buscabinaria(array, i, media - 1, m, menor)
    else:
        return menor


lista = list(map(int, input().split(' ')))
quantidadeArvores = lista[0]
quantidadeMadeiras = lista[1]

arvores = list(map(int, input().split(' ')))
arvores.sort()

indice = buscabinaria(arvores, 0, quantidadeArvores - 1, quantidadeMadeiras)
print(arvores[indice])