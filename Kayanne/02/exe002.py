lista_numeros = list() #criada lista vazia
lista_metade = list() #criada lista vazia
for i in range(0, 11):
    #forma direta -> valor = lista_numeros.append(int(input(f'Digite um valor, por favor: ')))

    valor = int(input(f'Digite um valor, por favor: '))
    
    lista_numeros.append(valor)

for j in lista_numeros:
    lista_metade.append((j / 2))

print(lista_metade)