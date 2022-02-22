diametro = int(input())
dimensoes = input().split()

altura = int(dimensoes[0])
largura = int(dimensoes[1])
profundidade = int(dimensoes[2])
naoCabe = 'S'

if(diametro > altura or diametro > largura or diametro > profundidade):
    naoCabe = 'N'

print(naoCabe)
