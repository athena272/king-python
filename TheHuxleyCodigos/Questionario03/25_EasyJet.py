largura = float(input())
comprimento = float(input())
altura = float(input())

ehPermitida = 'PERMITIDA'

if(largura > 45 or comprimento > 56 or altura > 25):
    ehPermitida = 'PROIBIDA'

print(ehPermitida)