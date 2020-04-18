from math import sqrt, pow, hypot
cat_op = float(input('Digite o valor do cateto oposto: '))
cat_adj = float(input('Digite o valor do cateto adjacente: '))
hipo = pow(cat_adj, 2) + pow(cat_op,2)
print('Nesse triângulo retângulo o valor da hipotenusa é {:.2f}'.format(sqrt(hipo)))
print('----ANOTHER----WAY----')
cateto_oposto = float(input('Quanto vale o cateto oposto?: '))
cateto_adjaecente = float(input('Quanto vale o cateto adjacente?: '))
#funçao que calcula automaticamente
hipotenusa = hypot(cateto_oposto, cateto_adjaecente)
print('O valor da Hipotenusa é {:.2f}'.format(hipotenusa))