def contVogais(texto):
    qtdVogais = 0
    for letra in texto:
        if (letra in 'aeiou'):
            qtdVogais += 1

    return qtdVogais

qtdVogais = 0
qtdPalavras = 0
textoVazio = 'texto vazio'
while True:
    texto = input().lower()

    if (texto == 'fim'):
        break

    qtdVogais += contVogais(texto)
    qtdPalavras += len(texto.split())



if(qtdPalavras == 0):
    print(textoVazio)

else:
    media = qtdVogais / qtdPalavras
    print('%.2f' % media)