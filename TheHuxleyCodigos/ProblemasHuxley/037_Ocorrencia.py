listaValores = input().split()

numeros = listaValores[0]
numeroProcurar = listaValores[1]

qtd = 0
for i in numeros:
    if i in numeroProcurar:
        qtd += 1

print(qtd)