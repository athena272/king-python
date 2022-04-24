quant = int(input())
valores = input().split()
strs = ''

novaLista = []

for num in valores:
    if num not in novaLista:
        novaLista.append(num)
        
listaFinal = [int(x) for x in novaLista]

listaFinal.sort( )
for num in listaFinal:
    strs = strs + str(num)  + " "

print(strs)