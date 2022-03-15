def maisBarato(gasolinaBR, gasolinaEUA):
    comparacao = 'Igual'
    if(gasolinaBR < gasolinaEUA):
        comparacao = 'Mais barata no Brasil'
    elif(gasolinaEUA < gasolinaBR):
        comparacao = 'Mais barata nos EUA'

    return comparacao


gasolinaDolar = float(input())
gasolinaReal = float(input())
cotacaoDolar = float(input())

dolarToReal = (gasolinaDolar * cotacaoDolar) / 3.8
quemMaisBarato = maisBarato(gasolinaReal, dolarToReal)


print('Gasolina EUA: R$ %.2f' %dolarToReal)
print('Gasolina Brasil: R$ %.2f' %gasolinaReal)
print(quemMaisBarato)