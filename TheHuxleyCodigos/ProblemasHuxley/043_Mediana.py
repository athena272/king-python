numeros = input().split()
novaList = list()
for i in numeros:
    novaList.append(int(i))
novaList.sort()
qtdNumeros = len(numeros)

mediana = novaList[(qtdNumeros - 1)// 2]
if (qtdNumeros % 2 == 0):
    n1 = float(novaList[(qtdNumeros - 1)// 2])
    n2 = float(novaList[(qtdNumeros) // 2])
    mediana = (n1 + n2) / 2

print('Mediana =',mediana)
