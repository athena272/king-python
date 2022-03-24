salario = float(input())


if(salario <= 280):
    salario += salario * 0.2

elif(salario > 280 and salario <= 780):
    salario += salario * 0.15

elif(salario > 780 and salario <= 1500):
    salario += salario * 0.1

else:
    salario += salario * 0.05

print(salario)