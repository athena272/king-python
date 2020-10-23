lista_numeros = list()
maior = 0
menor = 0
#Adicionar valores em uma lista
for i in range(0, 5):
    lista_numeros.append(int(input(f"Digite um valor para a posicao {i}: ")))
print('-=' * 30)
print(f'A lista foi {lista_numeros}') #Imprimirar a lista
#-----------------------------------------------
print(f'O maior valor foi {max(lista_numeros)} nas posições ', end='')
#Saber a posição dos maiores
for pos, elemento in enumerate(lista_numeros):
    if (elemento == max(lista_numeros)):
        print(f'{pos}...', end='')
#-----------------------------------------------
print(f'\nO menor valor foi {min(lista_numeros)} nas posições ', end='')
for pos, elemento in enumerate(lista_numeros):
    if (elemento == min(lista_numeros)):
       print(f'{pos}...', end='')
