numeros = input().split()

A = int(numeros[0])
B = int(numeros[1])

subtrair = 0
i = 0

while True:
    subtrair = A - (2 ** i)

    if(subtrair == B):
        break;