def convertListInt(listaString):
    listaInt = list()
    for i in listaString:
        listaInt.append(int(i))

    return listaInt

listaNumeros = input().split()
listaNumeros = convertListInt(listaNumeros)
listaNumeros.sort(reverse=True)

maiorNumero = listaNumeros[0]
print(maiorNumero)