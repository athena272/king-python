texto = input()
aparicoes = {}
listaCaracter = []
for letra in texto:
    aparicoes[letra] = aparicoes.get(letra,0)+1

for caracter in aparicoes:
    listaCaracter.append(caracter)

listaCaracter.sort()
novalista = listaCaracter[::-1]

for elemento in novalista:
    print(elemento,aparicoes[elemento])