from time import sleep
velocity= float(input('Qual a velocidade do carro?: '))
print('zzzzoooommmmmm....')
sleep(4)
if velocity > 80:
    print('''                 BAAAAAMMMMMMMM
    Você está indo muito rápido, SERÁ MULTADO
                     TABELINHA DA MULTA
                     MULTA | Km/h
                     ------|----
                     R$7,00| 1 Km/h''')
    multa= (velocity - 80) * 7
    print('----SUA--MULTA------'
          '\nSua multa será de R${:.2f}'.format(multa))