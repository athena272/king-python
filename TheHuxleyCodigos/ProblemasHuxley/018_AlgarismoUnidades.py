num = int(input())

algarismoUnidade = num % 10

if(num < 0):
    algarismoUnidade = -1 * (abs(num) % 10)

print('Digite um numero:')
print('Algarismo das unidades:', algarismoUnidade)
