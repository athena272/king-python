palavra = input()
letra = input()

qtdLetras = 0
for letraPalavra in palavra:
    if(letraPalavra == letra):
        qtdLetras += 1

print(qtdLetras)