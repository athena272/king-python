def tirarEspecias(palavra):
    palavraNormal = ''
    for letra in palavra:
        if (letra not in '."(*$#:'):
            palavraNormal += letra

    return palavraNormal

dicionarioPalavras = dict()
while True:
    
    texto = input()
    if(texto == '-1'):
        break
    if(texto == ''):
        continue

    texto = tirarEspecias(texto)
    texto = texto.lower().split()

    for palavra in texto:
        dicionarioPalavras[palavra] = dicionarioPalavras.get(palavra, 0) + 1
    
    dicionarioPalavras = sorted(dicionarioPalavras.items())

for palavraDic, apariacao in dicionarioPalavras:
    print(palavraDic,'-',apariacao) 

    