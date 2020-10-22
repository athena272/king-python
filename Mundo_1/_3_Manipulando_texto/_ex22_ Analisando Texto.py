#pedir nome completo
name= input('Qual seu nome completo, por favor?: ').strip()
#Imprimir tudo maiúsculo
print('Seu nome em maiúsculo é {}'.format(name.upper()))
#imprimir todo minusculo
print('Seu nome em minusculo é {}'.format(name.lower()))
#letras no nome
print('Seu nome tem {} letras'.format(len(name) - name.count(' ')))
#letras do primeiro nome
dividir= name.split()
print('Seu primeiro nome é {} e este tem {} letras'.format(dividir[0],len(dividir[0])))