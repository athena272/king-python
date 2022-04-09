def convertListInt(listaString):
    listaInt = list()
    for i in listaString:
        listaInt.append(int(i))

    return listaInt


def removeRepetidos(listaNum):
    listaSemRepetidos = list()
    for elem in listaNum:
        if elem not in listaSemRepetidos:
            listaSemRepetidos.append(elem)
    
    return listaSemRepetidos

qtdNumeros = int(input())
listaNumeros = input().split()
listaFinal = removeRepetidos(listaNumeros)
listaFinal = convertListInt(listaFinal)

textoFinal = ''
listaFinal.sort()
for i in listaFinal:
    textoFinal += str(i) + ' '

print(textoFinal)


