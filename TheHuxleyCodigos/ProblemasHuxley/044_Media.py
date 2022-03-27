numeros = input().split()

novaList = list()
for i in numeros:
    novaList.append(int(i))
novaList.sort()

qtdNumeros = len(numeros)

soma = 0
for j in novaList:
    soma += j

media = soma / qtdNumeros

print('Media = %.1f' %media)