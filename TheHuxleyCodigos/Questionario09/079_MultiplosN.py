numMultiplo = int(input())
limiteInferior = int(input())
limiteSuperior = int(input())

comeco = 'INEXISTENTE'

if(numMultiplo > limiteSuperior):
    print("INEXISTENTE")
else:
    for comeco in range(limiteInferior, limiteSuperior + 1):
        multiploN = (comeco % numMultiplo == 0)
        if(multiploN):
            print(comeco)

