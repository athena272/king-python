salary= float(input())
percentual = float(input()) 

reajuste = salary + (salary * (percentual / 100))

print('Seu salario teve aumento de ' +  str(percentual) + ' %, passando de R$ ' + str(salary) + ' para R$ ' + str(reajuste))