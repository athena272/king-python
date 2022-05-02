qtdLeituras = int(input())
for i in range(qtdLeituras):
    qtdAlimento = float(input())
    qtdDias = 1
    while(qtdAlimento / 2 > 1):
        qtdDias += 1
        qtdAlimento = qtdAlimento / 2
    print(qtdDias, 'dias')