listaNumeros = list()
for i in range(0, 101):
    numero = int(input())
    listaNumeros.append(numero)

numeroGetIndex = listaNumeros[-1]
posAparicoes = [indice for indice, numero in enumerate(listaNumeros) if (numero == numeroGetIndex and indice != len(listaNumeros) - 1)]

for pos in posAparicoes:
    print(pos)


    