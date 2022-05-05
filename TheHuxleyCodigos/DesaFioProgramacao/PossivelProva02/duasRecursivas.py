def temSoPositivo(listaNum, i = 0):
    if(listaNum[i] < 0):
        return False

    if(i == len(listaNum) - 1):
        return True
    
    return temSoPositivo(listaNum, i + 1)

def entre5e10(listaNum, i = 0,):
    if(i == len(listaNum)):
        return 0

    if(listaNum[i] >= 5 and listaNum[i] <= 10):
        return 1 + entre5e10(listaNum, i + 1)

    else:
        return 0 + entre5e10(listaNum, i + 1)

listaNumeros = input().split()
listaNumeros = [int(i) for i in listaNumeros]
 
if(temSoPositivo(listaNumeros) == False):
    print('ha nao positivo')

else:
    print(entre5e10(listaNumeros))
    