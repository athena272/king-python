def ehImpar(valor):
    serImpar = False
    if(valor % 2 != 0):
        serImpar = True
    
    return serImpar

valor1 = int(input())
valor2 = int(input())

contador = valor1
while (contador <= valor2):
    if(ehImpar(contador)):
        print(contador)

    contador = contador + 1#aumentar de um em um
    