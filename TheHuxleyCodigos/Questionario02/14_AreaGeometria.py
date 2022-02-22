ladosTriangulo = input().split()

#Valores que serao trabalhados
PI = 3.14159
ladoA = float(ladosTriangulo[0])
ladoB = float(ladosTriangulo[1])
ladoC = float(ladosTriangulo[2])

#Valores para saida
areaTriangulo = (ladoA * ladoC) / 2
areaCirculo = PI * ladoC ** 2
areaTrapezio = ((ladoA + ladoB) * ladoC) / 2
areaQuadrado = ladoB ** 2
areaRetangulo = ladoA * ladoB

#Saida com prints
print('TRIANGULO: %.3f' %areaTriangulo)
print('CIRCULO: %.3f' %areaCirculo)
print('TRAPEZIO: %.3f' %areaTrapezio)
print('QUADRADO: %.3f' %areaQuadrado)
print('RETANGULO: %.3f' %areaRetangulo)


