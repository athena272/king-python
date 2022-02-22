valor = int(input())

ehNegativo = 'NEGATIVO'
ehImpar = 'IMPAR'

if(valor == 0): #Caso seja 0, acaba ai mesmo e so eh nulo
    ehNegativo = 'NULO'
    print(ehNegativo)

else: #Senao, eh so verificar 
    if(valor > 0):
        ehNegativo = 'POSITIVO'

    if(valor % 2 == 0):
        ehImpar = 'PAR'

    print(ehNegativo, ehImpar)

