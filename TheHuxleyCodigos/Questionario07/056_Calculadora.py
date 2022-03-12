def calcular(valor1, valor2, operador):
    calculo = valor1 / valor2
    if(operador == '+'):
        calculo = valor1 + valor2
    elif(operador == '-'):
        calculo = valor1 - valor2
    elif(operador == '*'):
        calculo = valor1 * valor2
    
    return calculo 

#Primeira iteracao
valor1 = int(input())
valor2 = int(input())
operador = input()
primeiroResult = calcular(valor1, valor2, operador)
print('%.3f' %primeiroResult)
#Inicio do laco
resultadoLoop = primeiroResult
while True:
    valorLoop = int(input())
    operador = input()
    if(operador == '&'): #Parar caso venha '&' como operador, parar!
        break
    elif(valorLoop == 0 and operador == '/'): #Caso seja divisao por zero
        print('operacao nao pode ser realizada')
        continue
    
    resultado = calcular(resultadoLoop, valorLoop, operador)    
    print('%.3f' %resultado)
    resultadoLoop = resultado
