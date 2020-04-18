valor1 = (int(input('Digite um número: ')),
          int(input('Digite mais um valor: ')),
          int(input('Digite outro valor: ')),
          int(input('Digite um último valor: ')))
print('Você digitou os valores: ',end='')
for i in valor1:
    print(f' {i} ',end='')
aparece_9 = valor1.count(9)
if (aparece_9 == 0):
    print('\nO número 9 não apareceu')
else:
    print(f'\nO número  9 apareceu {aparece_9} vez(es)')
if (valor1.count(3) == 0):
    print('O número 3 não apareceu')
else:
    pos_3 = valor1.index(3) + 1
    print(f'O número 3 apareceu na {pos_3}ª posição')
print('Os valores pares digtados foram: ',end='')
contador = 0
for pares in valor1:
    if (pares % 2 == 0):
        print(f' {pares} ',end='')
        contador += 1
if (contador == 0):
    print('\033[1;31mNão houveram valores pares!\033[m', end='')