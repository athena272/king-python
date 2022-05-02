def convertListInt(listaString):
    listaInt = list()
    for i in listaString:
        listaInt.append(int(i))

    return listaInt

num = int(input())
if (num <= 1):
    print(0)
else: 
    pos_1 = 0
    pos_2 = 1

    cont = 3
    listaNumeros = [0, 1]
    while (cont <= num):
        pos_3 = pos_2 + pos_1
        listaNumeros.append(pos_3)
        pos_1 = pos_2
        pos_2 = pos_3
        cont += 1

    listaNumeros.sort(reverse=True)
    textoSaida = ""
    for i in listaNumeros:
        textoSaida += str(i) + " "
    texto = " ".join(textoSaida.split())
    
    print(texto)