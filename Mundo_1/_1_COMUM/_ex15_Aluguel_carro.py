day= int(input('Por quantos dias você alugou o carro?: '))
km= float(input('Quantas quilômetros(Km) vocÊ rodou com o carro?: '))
total= (day*60) + (km*0.15)
print('=== TOTAL A SER PAGO ==='
      '\nDIÁRIA ==== R$60'
      '\nPOR KM ==== R$0.15 ')
print('Você usou o carro por {} dias'
      '\nVocê percorreu {} quilômetros(Km)'
      '\nVocê irá pagar no total R${:.2f} '.format(day, km, total))
