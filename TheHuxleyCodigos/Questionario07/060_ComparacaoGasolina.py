gasolinaDolar = float(input())
gasolinaReal = float(input())
cotacaoDolar = float(input())

dolarToReal =  gasolinaDolar / cotacaoDolar
galaoToLitro = (dolarToReal * 3.8) 


print('Gasolina EUA: R$')
print('Gasolina Brasil: R$ %.2f' %gasolinaReal)
print(galaoToLitro)
print(dolarToReal)