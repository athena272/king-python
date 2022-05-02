def ehPrimo(num, i = 2):
     
    # Base cases
    if (num <= 2):
        return True if(num == 2) else False
    if (num % i == 0):
        return False
    if (i * i > num):
        return True
 
    # Check for next divisor
    return ehPrimo(num, i + 1)

listaNumeros = input().split()
qtdNumPrimos = 0
produtoPrimos = 1
for num in listaNumeros:
    if(ehPrimo(int(num))): 
        qtdNumPrimos += 1
        produtoPrimos *= int(num)

if(qtdNumPrimos == 4):
    print(produtoPrimos)
else:
    print('SEM PRODUTO')
