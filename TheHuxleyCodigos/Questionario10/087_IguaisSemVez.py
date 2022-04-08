def removeRepetidos(listaNum):
    listaSemRepetidos = list()
    for elem in listaNum:
        if elem not in listaSemRepetidos:
            listaSemRepetidos.append(elem)
    
    return listaSemRepetidos

qtdNumeros = int(input())
listaNumeros = input().split()
listaFinal = removeRepetidos(listaNumeros)

textoFinal = ''
listaFinal.sort()
for i in listaFinal:
    textoFinal += i + ' '

print(textoFinal)


