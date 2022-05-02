def tudoContrario(lista):
    if len(lista) <= 1:
        return lista
    else:
        return lista[-1:] + tudoContrario(lista[:-1])
    
listaNumeros = []
while True:
    num = int(input())
    if num == 0:
        break
    listaNumeros.append(num)

for n in tudoContrario(listaNumeros):
    print(n)