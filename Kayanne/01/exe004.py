somaPares = 0
multImpares = 1
contador = 1

while True:
    num = int(input(f'Digite o {contador}º número [maiores que 1000 fazem parar]: '))
    
    if (num > 1000): #caso a pessoa digite o numero maior que 1000
        break #sair e parar o laço
    
    if (num % 2) == 0: #verificar se é par
        somaPares = somaPares + num #soma = soma + num
    
    else: #se nao eh par, entao so pode ser impar
        multImpares = multImpares * num # mult = mult * num
  
    contador = contador + 1 #incrementar o contador

print(f'\nA soma de todos os números pares é {somaPares}'
       f'\n\nA multiplicação de todos os números ímpares é {multImpares}')

       