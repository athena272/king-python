def listaPosMais1(qtdElement, listaString):
    lista = listaString[1:qtdElement] + [listaString[0]]

    espaco = ' '
    texto = espaco.join(lista)
    return texto

def listaInversa(qtdElement, listaString):
    cont = qtdElement - 1
    listaInversa = list()
    while cont >= 0:
        listaInversa.append(listaString[cont])
        cont -= 1
    
    espaco = ' '
    texto = espaco.join(listaInversa)
    return texto


def convertListInt(listaString):
    listaInt = list()
    for i in listaString:
        listaInt.append(int(i))

    return listaInt


def listaDecrescente(listaNum):
    listaNum.sort(reverse=True)

    texto = ''
    for elem in listaNum:
        texto += str(elem) + ' '
    
    return texto


#Receber a lista de numeros
qtdElement = int(input())
listaNumeros = input().split()

listaReversa = listaInversa(qtdElement, listaNumeros)
listaEsquerda = listaPosMais1(qtdElement, listaNumeros)

listaNumeros = convertListInt(listaNumeros)
listaDecre = listaDecrescente(listaNumeros)

print(listaReversa)
print(listaEsquerda)
print(listaDecre)