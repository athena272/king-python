#Link repositorio: https://github.com/athena272/BNE_TI

def fat(num):
    if num == 0:
        return 1 

    fatorial = num * fat(num - 1)
    return fatorial


#Constroi o texto da somatoria
numerador = 100
denominador = 1
texto = ""
for i in range(0, 16):
    
    if(i != 15):
        texto += "(" + str(numerador) + "/" + str(denominador) + "!)" + " + "
    #evitar o sinal de "+" no ultimo caso
    else:
        texto += "(" + str(numerador) + "/" + str(denominador) + "!)"
    numerador -= 2
    denominador += 1

print(texto, end=" = ")

#Calcula a somatoria
numerador = 100
denominador = 1
somatoria = 0
cont = 0
while(cont <= 15):
    somatoria += (numerador/(fat(denominador)))
    
    numerador -= 2
    denominador += 1
    cont += 1
    
print(somatoria)

#Link repositorio: https://github.com/athena272/BNE_TI
