peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)
texto = 'IMC = %.4f' % imc
#verificar se tem ponto floante
numero = str(imc).split('.')
if(numero[-1] == '0'):
        imc = imc // 1
        texto = 'IMC = %0.f' % imc


print('Digite a massa em Kg:')
print('Digite a altura em m:')
print(texto)