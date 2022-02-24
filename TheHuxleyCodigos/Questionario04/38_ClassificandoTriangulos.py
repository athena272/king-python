lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

tipoTriangulo = 'isosceles'

tresLadosDiferentes = (lado1 != lado2 and lado1 != lado3 and lado2 != lado3)

if (lado1 == lado2 == lado3):
    tipoTriangulo = 'equilatero'
elif (tresLadosDiferentes):
    tipoTriangulo = 'escaleno'

print(tipoTriangulo)