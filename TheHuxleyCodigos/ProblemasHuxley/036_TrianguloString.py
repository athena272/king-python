texto = input().upper()

tamanho = len(texto)

while tamanho > 20 or texto == '':
    print('Entrada invalida')
    texto = input().upper()
    tamanho = len(texto)

cont = 1
for i in texto:
    print(i * cont)
    cont += 1
