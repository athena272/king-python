cont = 0
totalDepositado = 0
diasMeta = 0
while cont < 7:
    valorDepositado = float(input())
    totalDepositado += valorDepositado
    
    if(cont == 0):
        cont += 1
        diaAnterior = valorDepositado
        continue
    
    if(valorDepositado >= (diaAnterior + 0.5)):
        diasMeta += 1
    
    diaAnterior = valorDepositado
    cont += 1

print('R$ %.2f' %totalDepositado)
print(diasMeta)