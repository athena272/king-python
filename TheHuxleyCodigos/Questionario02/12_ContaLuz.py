consumoEnergia = float(input())

contaLuz = consumoEnergia * 1.50
contaDesconto = contaLuz - (contaLuz * 0.15)

print('Valor a ser pago: R$ %.2f reais' %contaLuz)
print('Valor a ser pago com desconto: R$ %.2f reais' %contaDesconto)



