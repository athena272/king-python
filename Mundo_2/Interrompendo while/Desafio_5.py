print('==== LISTA DE COMPRAS ===')
numero_produto = 1
total_gasto = 0
produto_maior_1000 = 0
menor = 0
menor_name = ''
while True:
    print('-=' * 20)
    print(f'{numero_produto}º \033[1;34mPRODUTO\033[m'.center(35))
    name_produto = str(input('DIgite o nome do produto: ')).strip().capitalize()
    preco_produto = float(input('Preço Produto: R$'))
    total_gasto += preco_produto
    if (preco_produto > 1000):
        produto_maior_1000 += 1
    if (numero_produto == 1):
        menor = preco_produto
        menor_name = name_produto
    else:
        if (preco_produto < menor):
            menor = preco_produto
            menor_name = name_produto
    print('--' * 20 )
    pergunta = str(input('Quer continuar? [s / n]: ')).strip().lower()[0]
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar? [s / n]: ')).strip().lower()[0]
    if (pergunta == 'n'):
        break
    numero_produto += 1
print('\n'
      f'O total gasto nas compras foi de R${total_gasto:.2f}'
      f'\nExistem {produto_maior_1000} produto(s) com mais de R$1000,00'
      f'\nO produto mais barato foi {menor_name} e custou R${menor}')

