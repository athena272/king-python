casa=float(input('Qual o valor da casa?: R$'))
sala=float(input('Qual seu salário, por favor?: R$'))
anos=int(input('Em quantos anos a casa será paga?:'))
salario_30=(sala*0.3)
prestacao= casa / (anos * 12)
print('Para pagar uma casa de R${} em {} anos'
      '\nHaverá uma prestação mensal de R${:.2f}'.format(casa, anos, prestacao))
print('''----------------
\033[33mPara afetuar o pagamento a prestação não deve ultrapassar 30% do seu salário:\033[m
O seu salário de R${:.2f} possui valor de 30% igual a R${:.2f}'''.format(sala, salario_30))
if prestacao > salario_30:
    print('---------------------'
          '\n\033[31;40mImpossível realizar o empréstimo, desculpe senhor!\033[m')
else:
    print('---------------------'
          '\n\033[32;40mSeu empréstimo foi aprovado com sucesso, parabéns senhor\033[m')
