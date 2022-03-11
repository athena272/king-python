valor1 = int(input())
valor2 = int(input())

limiteInferior = min(valor1, valor2) 
limiteSuperior = max(valor1, valor2)
somaPositivos = 0

while limiteInferior <= limiteSuperior:
    if(limiteInferior > 0):
        somaPositivos += limiteInferior # somaPositivos = somaPositivos + limiteInferior
    
    limiteInferior += 1

print(somaPositivos)
    

