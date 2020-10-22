sala = float(input('Qual o seu salário atual?: R$'))
if sala >= 1250:
    print('Seu salário é superior à R$1250,00 então haverá um aumento de 10%'
          '\n Seu novo salário é R${:.2f}'.format((sala*0.1)+sala))
else:
    print('Seu salário é inferior ou igual à R$1250,00 então haverá um aumento de 15%'
          '\nSeu novo salário é R${:.2f}'.format((sala*0.15)+sala))