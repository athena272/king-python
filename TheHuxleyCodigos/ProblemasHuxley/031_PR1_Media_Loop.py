limite = int(input())

if(limite < 0):
    print('Digite um numero positivo:')
    print('Apenas valores positivos')

else:
    soma = 0
    for i in range(0, limite + 1):
        soma += i

    media = soma / limite
    #verificar se tem ponto floante
    numero = str(media).split('.')
    if(numero[-1] == '0'):
         media = soma // limite

    print('Digite um numero positivo:')
    print(f'Media de 1 ate {limite}: {media}')
