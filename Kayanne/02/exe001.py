lista_numeros = list() #crio uma lista

for i in range(0, 50):
    ehImpar = (i % 2 != 0) #Resultado se numero eh par[True ou False]
    if ehImpar:
        lista_numeros.append(i)

print(lista_numeros)