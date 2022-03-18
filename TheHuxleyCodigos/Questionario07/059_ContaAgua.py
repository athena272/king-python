contaMetros = int(input())

totalPagar = 7
faixaConsumo11_30 = contaMetros - 10
faixaConsumo31_100 = contaMetros - 30
faixaConsumoMaior100 = contaMetros - 100
if(contaMetros >= 11 and contaMetros <= 30): 
    totalPagar += (1 * faixaConsumo11_30) 

elif(contaMetros >= 31 and contaMetros <= 100):
    totalPagar += 20#20 numeros entre 11 e 30, "encheu"
    totalPagar += (2 * faixaConsumo31_100)

elif(contaMetros > 100):
    totalPagar += 140 + 20 #70 vezes dois reais, 140 numeros entre 31 ate 100, mais 20 numeros de 11 ate 30
    totalPagar += (5 * faixaConsumoMaior100) 

print(totalPagar)
