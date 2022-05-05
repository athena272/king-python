def tiraInvalido(palavra):
    palavraValida = ''
    for letra in palavra:
        if (letra not in '."(*$#:'):
            palavraValida += letra

    return palavraValida

dicionarioPalavras = dict()
while True:
    
    texto = input()
    if(texto == '-1'):
        break
    if(texto == ''):
        continue

    texto = tiraInvalido(texto)
    texto = texto.lower().split()

    for palavra in texto:
        dicionarioPalavras[palavra] = dicionarioPalavras.get(palavra, 0) + 1
    
#Erro ao colocar o sorted no laco while, isso gera um tempo de execucao muito alto pois ficar colocando em ordem a cada execucao eh custoso
dicionarioPalavras = sorted(dicionarioPalavras.items())

for palavraDic, apariacao in dicionarioPalavras:
    print(palavraDic,'-',apariacao) 