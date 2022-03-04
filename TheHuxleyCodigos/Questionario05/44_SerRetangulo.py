#declaracao de funcoes
def ehRetangulo(lado1, lado2, lado3, lado4):
    isTriangulo = True

    if (lado1 != lado2 and lado1 != lado3 and lado1 != lado4):
        isTriangulo = False
    elif(lado1 != lado2 and lado2 != lado3 and lado2 != lado4):
        isTriangulo = False
    elif(lado3 != lado1 and lado3 != lado2 and lado3 != lado4):
        isTriangulo = False
    elif(lado4 != lado1 and lado4 != lado2 and lado4!= lado3):
        isTriangulo = False

    return isTriangulo


#entrada de dados
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())
lado4 = float(input())

textoRetangulo = 'NAO EH UM RETANGULO'

if(ehRetangulo(lado1, lado2, lado3, lado4)):
    textoRetangulo = 'RETANGULO'

print(textoRetangulo)