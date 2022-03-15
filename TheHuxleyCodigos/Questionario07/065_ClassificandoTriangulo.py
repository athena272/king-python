def serTriangulo(lado1, lado2, lado3):
    serTriangulo = 'INVALIDO'
    if(lado1 < (lado2 + lado3) and lado2 < (lado3 + lado1) and lado3 < (lado1 + lado2)):
        serTriangulo = classificaTriangulo(lado1, lado2, lado3)
    
    return serTriangulo

def classificaTriangulo(lado1, lado2, lado3):
    tipoTriangulo = 'ISOSCELES'

    tresLadosDiferentes = (lado1 != lado2 and lado1 != lado3 and lado2 != lado3)

    if (lado1 == lado2 == lado3):
        tipoTriangulo = 'EQUILATERO'
    elif (tresLadosDiferentes):
        tipoTriangulo = 'ESCALENO'

    return tipoTriangulo

while True:
    listaLados = input()
    if(listaLados == 'FIM'):
        break

    listaLados = listaLados.split()
    lado1 = int(listaLados[0])
    lado2 = int(listaLados[1])
    lado3 = int(listaLados[2])

    print(serTriangulo(lado1, lado2, lado3))
