def ePrimo(num):
    serPrimo = True
    #Se par, tirando o 2
    if(num >= 4 and num % 2 == 0):
        serPrimo = False
    else:
        for i in range(3, num):
            if(num % i == 0):
                serPrimo = False
                break
        
    return serPrimo

valor1 = int(input())
valor2 = int(input())

if(ePrimo(valor1) == False):
    print('O numero', valor1,'nao eh primo')
elif(ePrimo(valor2) == False):
    print('O numero', valor2,'nao eh primo')
else:
    soma = valor1 + valor2
    if(ePrimo(soma)):
        print('A soma de', valor1, 'e', valor2,'eh um primo')
    else:
        print('A soma de', valor1, 'e', valor2,'nao eh um primo')