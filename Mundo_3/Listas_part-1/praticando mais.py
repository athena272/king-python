lista1 = []
lista2 = list(range(5, 101, 5))
lista1.append(5)
lista1.append(19)
lista1.append(-33)
#lista1.sort(reverse=True)
for c, i in enumerate(lista1):
    print(f'Na {c+1}ª posição está o valor {i}...')

lista1 = lista2 #cria ligação
lista1 = [:]#cria uma cópia