def removeRepetidos(lista):
    novaLista = list()
    for i in lista:
        if i not in novaLista:
            novaLista.append(i) 
    novaLista.sort()
    return novaLista

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
frase = input().lower()

letras = list()
for letra in frase:
    if letra in alfabeto:
        letras.append(letra)

letras = removeRepetidos(letras)

for j  in letras:
    print(j)
