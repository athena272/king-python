day= int(input())
km= float(input())

diaria = 30 * day
kmPreco = 0.01 * km
porcento10 = (diaria + kmPreco) * 0.1
total = (diaria + kmPreco) - porcento10

print('Digite a quantidade de dias de locacao:')
print('Digite a quantidade de km rodados:')
print('Valor a pagar pelo aluguel: R$ %.6f' % total)