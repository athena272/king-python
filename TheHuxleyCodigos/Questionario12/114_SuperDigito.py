def superDigito(algarismos):
    if len(algarismos) == 1:
        return int(algarismos[0])
    
    soma = 0
    for num in algarismos:
        soma += int(num)
    
    return superDigito(quebraNumero(soma))
    
def quebraNumero(numero):
    numero = str(numero)
    listaAlgarismo = list()
    for i in numero:
        listaAlgarismo.append(i)

    return listaAlgarismo

def concatenacao(num, qtdConcat):
    listaConcat = list()
    for _ in range(qtdConcat):
        listaConcat += num
    
    return listaConcat

listaValores = input().split()
num = listaValores[0]
qtdConcatena = int(listaValores[1])
listaConcatenada = concatenacao(num, qtdConcatena)
print(superDigito(listaConcatenada))
