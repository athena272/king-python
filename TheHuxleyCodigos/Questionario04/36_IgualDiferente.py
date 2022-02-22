valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

qtdIguais = 3

if(valor1 == valor2 == valor3):
    qtdIguais = 1

elif(valor1 != valor2 != valor3):
    qtdIguais = 2

print(qtdIguais)