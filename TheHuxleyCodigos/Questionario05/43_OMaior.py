#declaracao de funcoes
def maiorAB(a, b):
    maior = (a + b + abs(a - b)) // 2
    return maior

#entrada de dados
    
listaValores = input().split()

valor1 = int(listaValores[0])
valor2 = int(listaValores[1])
valor3 = int(listaValores[2])

entreValor1_2 = maiorAB(valor1, valor2)

oMaior = maiorAB(entreValor1_2, valor3)

print(oMaior,'eh o maior')
