def convertListInt(listaString):
    listaInt = list()
    for i in listaString:
        listaInt.append(int(i))

    return listaInt

listaNumeros = input().split()
listaNumeros = convertListInt(listaNumeros)
maiorNumero = max(listaNumeros)

print(maiorNumero)