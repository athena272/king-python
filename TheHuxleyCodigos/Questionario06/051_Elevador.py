listaValores = input().split()

qtdLeituras = int(listaValores[0])
capacidadeMax = int(listaValores[1])

cont = 0
capacidadeExcedida = 'N' 
pessoasElevador = 0
while cont < qtdLeituras:
    leituras = input().split()
    qtdSairam = int(leituras[0])
    qtdEntraram = int(leituras[1])

    pessoasElevador = (pessoasElevador - qtdSairam) 
    pessoasElevador = (pessoasElevador + qtdEntraram)
    
    if(pessoasElevador > capacidadeMax):
        capacidadeExcedida = 'S'
    
    cont += 1

print(capacidadeExcedida)
