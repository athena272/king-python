peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)

texto = 'normal'
if imc < 18 or imc > 25:
    texto = 'atencao'

print('%.2f' % imc)
print(texto)