def findPercentual(qtdOpcao, qtdVotos):
    percentual = (qtdOpcao * 100) / qtdVotos
    return percentual


qtdAlibaba = 0
qtdAlcapone = 0
qtdBrancos = 0
qtdNulos = 0
ganhador = 93
while True:
    voto = int(input())
    if(voto == -1):
        break
    if(voto == 83):
        qtdAlibaba += 1
    elif(voto == 93):
        qtdAlcapone += 1
    elif(voto == 0):
        qtdBrancos += 1
    else:
        qtdNulos += 1

   

if(qtdAlibaba > qtdAlcapone):
    ganhador = 83

qtdVotos = qtdAlibaba + qtdAlcapone + qtdBrancos
percentualAlibaba = findPercentual(qtdAlibaba, qtdVotos)
percentualAlcapone = findPercentual(qtdAlcapone, (qtdAlibaba + qtdAlcapone + qtdBrancos))

print(qtdAlibaba)
print(qtdAlcapone)
print(qtdBrancos)
print(qtdNulos)
print(ganhador)
print('%.2f' %percentualAlibaba)
print('%.2f' %percentualAlcapone)


