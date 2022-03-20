def piramedeNumeros(num):
    texto = ''
    for i in range(1, num + 1):
        texto += ((str(i) + '-') * i) #Imprimir o mesmo numero 'i' vezes

        ultimoHifen = len(texto) - 1 #retirar o hifen no final
        texto = texto[0:ultimoHifen] 
        texto += '\n' #acrescentar o numero '\n' ao final de cada linha
    
    return texto

num = int(input())

print(piramedeNumeros(num))