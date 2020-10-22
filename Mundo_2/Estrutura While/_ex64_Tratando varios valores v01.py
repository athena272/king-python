num = 0
soma = 0
quantos = 0
while ( num != 999):
    num = int(input('Digite um número inteiro [999 faz parar]: '))
    if (num != 999):
        soma += num
        quantos += 1
print('\n'
      'Apareceram {} números'
      '\nE a soma de todos ele é igual a {}'.format(quantos, soma))