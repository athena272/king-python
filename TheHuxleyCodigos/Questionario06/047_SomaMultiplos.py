valor = int(input())

cont = 0
soma = 0
while cont < valor:
    mult3 = (cont % 3 == 0)
    mult5 = (cont % 5 == 0)
    if(mult3 or mult5):
        soma += cont

    cont += 1

print(soma)