def ehPrimo(numero):
    cont = 4
    serPrimo = True
    while cont < numero:
        if(numero % cont == 0):
            serPrimo = False
            break;
        
        cont += 1
    
    return serPrimo

qtdLeituras = int(input())
cont = 0
while cont < qtdLeituras:   
    listaValores = input().split()
    distancia = float(listaValores[0])
    precoKm = float(listaValores[1])

    valorPagar = (distancia * precoKm)
    valorPagarInteiro = valorPagar // 1
    if(ehPrimo(valorPagarInteiro)):
        valorPagar = valorPagar - (valorPagar * 0.42)

    print('%.2f' %valorPagar)
    cont += 1