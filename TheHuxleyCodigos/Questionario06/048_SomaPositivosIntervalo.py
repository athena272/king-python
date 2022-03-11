valor1 = int(input())
valor2 = int(input())

limiteInferior = min(valor1, valor2)
limiteSuperior = max(valor1, valor2)

comeco = limiteInferior
soma = 0
while comeco <= limiteSuperior:
    if(comeco > 0):
        soma += comeco

    comeco += 1

print(soma)


   