l1=float(input('Quanto vale o primeiro lado?: '))
l2=float(input('Quanto vale o segundo lado?: '))
l3=float(input('Quanto vale o terceiro lado?: '))
if (l1 < l2+l3) and (l2 < l1+l3) and (l3 < l1+l2):
    print('É possível formar um trinângulo com essas medidas')
    if (l1 == l2) and (l2 == l3):
        print('É um triângulo EQUILÁTERO, todos os lados tem medidas iguais')
    elif (l1 != l2) and (l2 != l3) and (l3 != l1):
        print('É um triângulo ESCALENO, todos os lados tem medidas diferentes')
    else:
        print('É um triângulo ISÓCELES, pelo menos 2 lados tem medidas iguais')
else:
    print('NÃO É possível formar um trinângulo com essas medidas')