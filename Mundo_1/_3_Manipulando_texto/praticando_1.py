acertos= 0
for i in range(136,181):
    print('-----------'
          '\n{}° Questão'.format(i))
    acertou= input('Acertou?: ')
    if acertou == 's' or acertou == 'sim':
        acertos +=1
print('Você acertou {} questões'.format(acertos))