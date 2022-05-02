def ehMult3(num):
    estado = False
    if(num % 3 == 0):
        estado = True
    
    return estado


def fat(num):
    if num == 0:
        return 1 

    fatorial = num * fat(num - 1)
    return fatorial


def somatoriaS(numerador, denominador):
    if denominador == 0: 
        return (numerador/fat(denominador))

    somatoria = (numerador/fat(denominador)) + somatoriaS(numerador, denominador - 1)
    return somatoria

listaValorEntrada = list()
for i in range(0, 5):
    numero = int(input())
    listaValorEntrada.append(numero)

listaValorSaida = list()
for numeroLoop in listaValorEntrada:
    if(ehMult3(numeroLoop)):
        numeroSaida = fat(numeroLoop)
        listaValorSaida.append(numeroSaida)
    else:
        numeroSaida = somatoriaS(numeroLoop, numeroLoop)
        listaValorSaida.append(numeroSaida)

somatoriaFinal = sum(listaValorSaida)
print("%.2f" %somatoriaFinal)

