salario = float(input())

impostoRenda = 0
if(salario >= 2001 and salario <= 3000):
    impostoRenda = (salario - 2000) * 0.08
    print('R$ %.2f' %impostoRenda)
elif(salario >= 3001 and salario <= 4500):
    impostoRenda += (1000 * 0.08)
    impostoRenda += (salario - 3000) * 0.18
    print('R$ %.2f' %impostoRenda)
elif(salario > 4500):
    impostoRenda += (1000 * 0.08)
    impostoRenda += (1500 * 0.18)
    impostoRenda += (salario - 4500) * 0.28
    print('R$ %.2f' %impostoRenda)
else:
    impostoRenda = 'Isento'
    print(impostoRenda)

