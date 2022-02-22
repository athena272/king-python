#Faça um programa que leia 3 números inteiros e os imprima em ordem crescente.

listaValor = list()
for i in range(0, 3):
    valor = int(input())
    listaValor.append(valor)

listaValor.sort()

print(listaValor[0])
print(listaValor[1])
print(listaValor[2])



