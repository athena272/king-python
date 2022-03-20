def contar_vogais(vogais, palavra):
    qtdVogais = 0
    for letra in palavra:
        if(letra in vogais):
            qtdVogais += 1
    
    return qtdVogais

qtdLeituras = int(input())

for leituras in range(0, qtdLeituras):
    vogaisAlign = input()
    palavraAlign = input()
    quantasVogais = contar_vogais(vogaisAlign, palavraAlign)
    print(quantasVogais)