def desenhar_linha():
    print('-=' * 15)


cincovalores = []
maior = menor = 0
posica_menor = 0
posica_maior = 0
pos = 0
for i in range(0, 5):
    cincovalores.append(int(input(f'Digite um valor, ele estará na posição {pos} da lista: ')))
    pos += 1
print(f'A lista foi {cincovalores}')
for c, e in enumerate(cincovalores):
    if (c == 0):
        maior = e
        menor = e
        posica_menor = c
        posica_maior = c
    else:
        if (e > maior):
            maior = e
            posica_maior = c
        if (e < menor):
            menor = e
            posica_menor = c
cincovalores.sort()
desenhar_linha()
print(f'O menor valor é {cincovalores[0]} e está na posição {posica_menor} dessa lista'
      f'\nO maior valor é {cincovalores[len(cincovalores) - 1]} está na posição {posica_maior} dessa lista')