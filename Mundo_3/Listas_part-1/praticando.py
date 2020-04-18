lista = ['lasanha', 'fritas', 'hamburguer']
lista.insert(1, 'salada')
del lista[3]
lista.pop(2)
print(lista)
if 'lasanha' in lista:
    print('\nContinua aqui')
#criar lista com range
nova_lista = list(range(0, 100, 5))
print(nova_lista)