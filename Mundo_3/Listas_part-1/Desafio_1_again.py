vlinha = ('=-' * 30)
cinco_valores= []
max_valor = min_valor = 0
posicao_maior = 0
posicao_menor = 0
pozicao = 0 #escreve errado de zoeira, me deixem matar o português
for i in range(0, 5):
    cinco_valores.append(int(input(f'Digite o {pozicao+1}º valor: ')))
    pozicao += 1
for c, e in enumerate(cinco_valores): #a variável "c" representa as vezes em ordem odinal que percorremos a lista
    if (c == 0):
        min_valor = e #"e" são os números da lista
        max_valor = e
        posicao_menor = c
        posicao_maior = c
    else:
        if (e > max_valor): #if (max_valor < e):
            max_valor = e
            posicao_maior = c
        if (e < min_valor): #(min_valor > e)
            min_valor = e
            posicao_menor = c
print(f'A lista foi \033[1;34m{cinco_valores}\033[m'
      f'\n\033[1;36m{vlinha}\033[m'
      f'\nO maior da lista foi \033[1m{max_valor}\033[m e é {posicao_maior+1}º número'
      f'\nO menor da lista foi \033[1m{min_valor}\033[m e é {posicao_menor+1}º número')


