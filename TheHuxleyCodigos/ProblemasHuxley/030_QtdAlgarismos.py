algarismos = input().split()

qtdAlgarismos = len(algarismos[-1])

textoOutput = 'O número possui ' + str(qtdAlgarismos) + ' algarismos!'

if(qtdAlgarismos > 5):
    textoOutput = 'Entrada incorreta!'

print(textoOutput)