lista_products = ('Computador', 2100,
                  'Impressora', 750,
                  'Mouse', 35.75,
                   'Teclado', 20.20,
                  'SSD', 450)
print('\033[1;33m--\033[m' * 20)
print(f'{"LOJAS GUIGO":^40}')
print('\033[1;33m--\033[m' * 20)
for posicao in range(0, len(lista_products)):
    if (posicao % 2 == 0):
        print(f'{lista_products[posicao]:.<25}',end='')
    else:
        print(f'R$ {lista_products[posicao]:.2f}')
print('\n'
      f'{" === FIM LISTA ==="}')