full_lista = list()
lista_pares = [] #Lista de valores pares
lista_impares = []  #lista de valores impares
while True:
    valor = full_lista.append(int(input('Digite um valor: ')))
    #Encerrar laço
    continuar = str(input('Deseja continuar?[S/N]: ')).lower().strip()[0]
    if (continuar == 'n'):
        break
##Valores impares e valores pares
for i in full_lista:
    if (i % 2 == 0):
        lista_pares.append(i)
    else:
        lista_impares.append(i)
print('-=' * 30)
print(f'A lista completa é {full_lista}'
      f'\nA lista com valores pares é {lista_pares}'
      f'\nA lista com valores impares é {lista_impares}')

      