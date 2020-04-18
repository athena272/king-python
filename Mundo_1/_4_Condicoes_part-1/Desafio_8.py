l1=float(input('Quanto vale o primeiro lado?: '))
l2=float(input('Quanto vale o segundo lado?: '))
l3=float(input('Quanto vale o terceiro lado?: '))
if (l1 < l2+l3) and (l2 < l1+l3) and (l3 < l1+l2):
    print('É possível formar um trinângulo com essas medidas')
else:
    print('NÃO É possível formar um trinângulo com essas medidas')