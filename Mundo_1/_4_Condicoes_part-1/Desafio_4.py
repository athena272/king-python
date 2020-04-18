#hora de viajar
kilometros= float(input('Qual a distância da viagem em quilômetros(Km), por favor: '))
print('''Tabelinha da passagem
         Distância da  | Preço por 
         viagem em (Km)|    (Km)
         --------------|----------
         Até 200 Km    |  R$0,50
         > que 200 Km  |  R$0,45
         --------------------------''')
preco_50= kilometros * 0.50
preco_45= kilometros * 0.45
if kilometros <= 200:
    print('Vocé fara uma viagem de {}Km com R$0.50 por (Km)'
          '\nO preço da sua viagem será de R${:.2f} com R$0.50 por (Km)'.format(kilometros,preco_50))
else:
    print('Vocé fara uma viagem de {}Km com R$0.45 por (Km)'
          '\nO preço da sua viagem será de R${:.2f} com R$0.45 por (Km)'.format(kilometros,preco_45))