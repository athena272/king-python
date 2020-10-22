pergunta = 's'
somar = 0
quantidade = 0
maior = 0
menor = 0
while (pergunta == 's'):
    num = int(input('Digite um valor: '))
    somar += num
    quantidade += 1
    if (quantidade == 1):
        maior = num
        menor = num
    else:
        if (num > maior):
            maior = num
        if (num < menor):
            menor = num
    print('---CONTINUAR ?---'.center(50))
    pergunta = str(input('Deseja digitar outro valor? [s / n]: ')).strip().lower()[0]
media = somar / quantidade
print('------RESULTADOS------'.center(50))
print('\n'
      'A soma de todos os {} números foi de {}, logo sua média é {:.2f}'
      '\nO maior valor é: {}'
      '\nO menor valor é: {}'.format(quantidade, somar, media, maior, menor))