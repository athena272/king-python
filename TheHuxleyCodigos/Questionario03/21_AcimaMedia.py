valor1 = float(input())
valor2 = float(input())
valor3 = float(input())

media = (valor1 + valor2 + valor3) / 3
acimaMedia = 0

if(valor1 > media):
    acimaMedia += 1

if(valor2 > media):
    acimaMedia += 1
    
if(valor3 > media):
    acimaMedia += 1

print(acimaMedia)

