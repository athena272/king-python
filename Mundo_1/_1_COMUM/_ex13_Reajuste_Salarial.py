salary= float(input('Qual o seu salário atual?: '))
reajuste_15= salary + (salary * 0.15)
print('O salário atual de R${} com o reajuste de 15% passará a ser agora de RS{:.2f}'.format(salary, reajuste_15))