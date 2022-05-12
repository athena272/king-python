texto=input()
aparicoes={}
listadecaracter=[]
for letra in texto:
    aparicoes[letra]=aparicoes.get(letra,0)+1
for caracter in aparicoes:
    listadecaracter.append(caracter)
listadecaracter.sort()
novalista=listadecaracter[::-1]
for elemento in novalista:
    print(elemento,aparicoes[elemento])