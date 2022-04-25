tamanhoArray = int(input())

primeiroArray = list()
for i in range(0, tamanhoArray):
    valores1 = int(input())
    primeiroArray.append(valores1)

segundoArray = list()
for j in range(0, tamanhoArray):
    valores2 = int(input())
    segundoArray.append(valores2)

listaIntercalada = list()
for k in range(0, tamanhoArray):
    listaIntercalada.append(primeiroArray[k])
    listaIntercalada.append(segundoArray[k])

for p in listaIntercalada:
    print(p)

    