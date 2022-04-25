def convertListInt(listaString):
    listaInt = list()
    for i in listaString:
        listaInt.append(int(i))

    return listaInt

qtdLeituras = int(input())
listaNumeros = input().split()
listaNumeros = convertListInt(listaNumeros)
menorNumero = min(listaNumeros)
posMenorNumero = listaNumeros.index(menorNumero)

print("Menor valor:", menorNumero)
print("Posicao:", posMenorNumero)