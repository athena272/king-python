def quantoPagar(qtdPaes, qtdBroas, formaPagamento):
    dinheiroPaes = qtdPaes * 0.5
    dinheiroBroas = qtdBroas * 2.30
    totalPagar = dinheiroPaes + dinheiroBroas
    
    if(formaPagamento == 'C'):
        totalPagar = totalPagar + (totalPagar * 0.05)
    
    return totalPagar

dinheiroArrecadado = 0
while True:
    listaValores = input().split()
    if(listaValores[0] == '*'):
        break;
    qtdPaes = int(listaValores[0])
    qtdBroas = int(listaValores[1])
    formaPagamento = (listaValores[2])
    
    totalPagar = quantoPagar(qtdPaes, qtdBroas, formaPagamento)

    dinheiroArrecadado += totalPagar
    

contaInvestir = dinheiroArrecadado * 0.1
print('Total arrecadado: R$%.2f' %dinheiroArrecadado, 'Conta investimento: R$%.2f' %contaInvestir)