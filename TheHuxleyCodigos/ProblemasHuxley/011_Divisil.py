# Faça um programa que indique se um número que o usuário digitou é divisível por 4 e por 7 ao mesmo tempo mas não divisível por 5.

# A saída deve ser um mensagem 'sim' ou 'nao' (minúsculos e sem o til).
num = int(input())

ehDivisivel = 'nao'

if(num % 4 == 0 and num % 7 == 0 and num % 5 != 0):
    ehDivisivel = 'sim'

print(ehDivisivel)