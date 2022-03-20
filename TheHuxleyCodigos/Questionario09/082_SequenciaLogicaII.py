listaValores = input().split()
num1 = int(listaValores[0])
num2 = int(listaValores[1])

texto = ''
for comeco in range(1, num2 + 1):
    multiploNum1 = (comeco % num1 != 0)
    texto += str(comeco) + ' ' if (multiploNum1) else str(comeco) + '\n'
print(texto)

