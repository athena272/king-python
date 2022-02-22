listaCasas = list()
while True:
    qtdVeiculo = int(input())
    if(qtdVeiculo == 999):
        break

    listaCasas.append(qtdVeiculo)

countCasa = 0
totalMulta = 0
for casa in listaCasas:
    if(casa > 2):
        multa = 12.89 * (casa - 2)
        totalMulta += multa
        countCasa += 1

print('%.2f' %totalMulta)
print(countCasa)