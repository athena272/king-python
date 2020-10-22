maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    print('-----------------------'
          '\n{}ª pessoa'.format(i))
    weight = float(input('Olá, por favor, digite o valor do seu peso (Kg): '))
    if (i == 1):
        maior_peso = weight
        menor_peso = weight
    else:
        if (weight > maior_peso):
            maior_peso = weight
        if (weight < menor_peso):
            menor_peso = weight
print('------------------------'
      '\nO maior peso encontrado foi {}Kg'
      '\nO menor peso encontrado foi {}Kg'.format(maior_peso, menor_peso))