altura = float(input())
raio = float(input())

PI = 3.14
areaBase = (PI * raio ** 2)
areaLateral = (2 * PI * raio * altura)
areaFinal = (2 * areaBase) + areaLateral
volume = areaBase * altura

print('%.2f' %volume)
print('%.2f' %areaFinal)

2352.79
1659.33