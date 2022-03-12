contaMetros = int(input())

totalPagar = 7
valorUnidades = contaMetros % 10
if(contaMetros >= 11 and contaMetros <= 30):
    tarifa = 30 - valorUnidades