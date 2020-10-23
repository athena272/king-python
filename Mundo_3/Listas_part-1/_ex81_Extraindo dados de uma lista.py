full_lista = list()
while True:
    valor = full_lista.append(int(input('Digite um valor, por favor: ')))
    continuar = str(input('Deseja continuar?[S/N]: ')).lower().strip()[0]
    if (continuar == 'n'):
        break
full_lista.sort(reverse=True) #colocar valores em ordem decrescente
print('-=' * 25)
print(f'Você digitou {len(full_lista)} elementos') #numero de elementos
print(f'Os valores em ordem descrescente são {full_lista}')
if (5 in full_lista):
    print('O valor 5 FAZ parte da lista!')
else:
    print('O valor 5 NÃO FAZ parte da lista!')