qtdPares = 0
qtdImpares = 0
qtdPositivos = 0
qtdNegativo = 0
while True:
    num = int(input())
    if(num == 0):
        break

    if(num % 2 == 0):
        qtdPares += 1
    else:
        qtdImpares += 1
    
    if(num > 0):
        qtdPositivos += 1
    else:
        qtdNegativo += 1

print('---------------------------')
print(qtdPares)
print(qtdImpares)
print(qtdPositivos)
print(qtdNegativo)
