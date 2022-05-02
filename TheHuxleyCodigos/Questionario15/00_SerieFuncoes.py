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

def proximoPrimo(num):
     
    if (ehPrimo(num + 1)):
        return num + 1
    
    return proximoPrimo(num + 1)

def fat(num):
    if num == 0:
        return 1 

    fatorial = num * fat(num - 1)
    return fatorial

def somatoria(num, numerador = 1, denominador = 1):
    if (numerador > denominador):
        denominador =  proximoPrimo(denominador)
    
    if numerador == num: 
        return (fat(numerador)/denominador)

    somatoriaS = (fat(numerador)/denominador) + somatoria(num, numerador + 1, denominador)
    return somatoriaS

def proximoPrimoString(i, denominador):
    if(i > denominador):
        denominador =  proximoPrimo(denominador)
    
    return str(denominador)

quantidade = int(input())
if (quantidade == 0):
    print("0.00")
else:
    texto = ''
    denominador = 1
    for i in range(1, quantidade + 1):
        if(i > denominador):
            denominador = proximoPrimo(denominador)

        texto += str(i) + "!/" + str(denominador) + " + "

    print(texto[0:len(texto)-3])
    saidaFinal = somatoria(quantidade)
    print("%.2f " %saidaFinal)

