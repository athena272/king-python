def removeRepetidos(palavra):
    listaSemRepetidos = [palavra[0]]
    letraAnterior = palavra[0]
    for letra in palavra[1:]:
        if letraAnterior != letra:
            listaSemRepetidos.append(letra)
        
        letraAnterior = letra
    
    return listaSemRepetidos


while True:
    frase = input()
    if frase == '*' : break
    if(frase == ''): continue
    frase = frase.split()
    textoSaida = list()
    for palavra in frase:
        semrep = removeRepetidos(palavra)
        juntaPalavra = ''.join(semrep)
        textoSaida.append(juntaPalavra)
    texto = " ".join(textoSaida)
    print(texto)