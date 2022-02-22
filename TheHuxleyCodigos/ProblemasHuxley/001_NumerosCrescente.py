#Receba dois números inteiros e os imprima em ordem crescente.

doisValores = input().split()

num1 = int(doisValores[0])
num2 = int(doisValores[1])

if(num1 < num2):
    print(num1, num2)
else:
    print(num2, num1)