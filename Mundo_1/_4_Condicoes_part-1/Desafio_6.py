#maior menor com lista
lista=[]
numero= str(input('Digite três números, por favor: ')).split()
print(numero)
for i in numero:
    i = int(i)
    lista.append(i)
lista.sort(reverse=True)
print('O maior número é [{}]'
      '\nO menor número é [{}]'.format(lista[0], lista[len(lista)-1]))
#modo Guanabara
a1 = int(input('Primeiro Valor: '))
a2 = int(input('Segundo Valor: '))
a3 = int(input('Terceiro Valor: '))
#verificar o maior
maior = a1
if a2 > a1 and a2 > a3:
    maior = a2
elif a3 > a1 and a3 > a2:
    maior = a3
#verificando menor
menor = a1
if a2 < a1 and a2 < a3:
    menor = a2
elif a3 < a1 and a3 < a2:
    menor = a3
print('O maior valor é [{}]'
      '\nO menor valor é [{}]'.format(maior,menor))