valor1 = int(input())
valor2 = int(input())

maiorMultiplo = 'sem multiplos menores que ' + str(valor2)
cont = valor1
while cont <= valor2:
    if(cont % valor1 == 0):
        maiorMultiplo = cont # somaPositivos = somaPositivos + limiteInferior
    
    cont += 1

print(maiorMultiplo)