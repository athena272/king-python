def calculoFracao(valor):
    calculo = (valor / (valor * 3))
    return calculo


def textoConcatenado(valor):
    texto = str(valor) + '/' + str(3 * valor) 
    return texto
 
qtdSerie = int(input())

cont = 1
somaSerie = 0
textoSerie = ''
while (cont <= qtdSerie):
    somaSerie += calculoFracao(cont) #faz o calculo de soma
    if(cont != qtdSerie): 
        textoSerie += textoConcatenado(cont) + ' + ' #Para todos os casos, coloca um + no texto'
    else:
        textoSerie += textoConcatenado(cont) #Mas no ultimo testo, o caractere '+' nao vem

    cont += 1

if(textoSerie != ''): #Se o texto vem vazio, nao precisa aparecer
    print(textoSerie)
print('%.2f' %somaSerie)
