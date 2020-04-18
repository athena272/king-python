print('=== Algoritmo que transforma reais em dólares ===')
dolar= float(input('Quanto reais você tem?:'))
novo_dinheiro= dolar/3.89
# onde há ":.2f" é para limitar o valor a duas casas decimais
print('Você tem {} reais\n Pela cotação mais atual do dólar, você possui {:.2f} dólares'.format(dolar, novo_dinheiro))