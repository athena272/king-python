#declaracao de funcoes
def ehRetangulo(lado1, lado2, lado3, lado4):
    isTriangulo = False
    if (lado1 == lado2 or lado2 == lado3 or lado3 == lado4):
        isTriangulo = True

    return isTriangulo

    
#entrada de dados
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())
lado4 = float(input())

print(ehRetangulo(lado1, lado2, lado3, lado4))