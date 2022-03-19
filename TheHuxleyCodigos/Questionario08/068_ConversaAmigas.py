def criptografarMensagem(indice):
    letraRetornar = ''
    cont = 0
    for letra in " abcdefghijqlmnopqrstuvwxyz":
        if(cont == indice):
            letraRetornar = letra
            break
       
        cont += 1
    
    return letraRetornar
        
while True:
    texto = ''
    mensagem = input().split()
    for palavra in mensagem:
        texto += criptografarMensagem(int(palavra))
    if(texto == 'fim'):
        break
    print(texto)


