def mediana(valor1, valor2, valor3):
    maior = max(valor1, valor2, valor3)
    menor = min(valor1, valor2, valor3)
    intermediario = valor1
    if(valor2 != maior and valor2 != menor):
        intermediario = valor2
    elif(valor3 != maior and valor3 != menor):
        intermediario = valor3
    
    return intermediario

num1 = int(input())
num2 = int(input())
num3 = int(input())

numIntermediario = mediana(num1, num2, num3)

print(numIntermediario)

