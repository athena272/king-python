def serPalindromo(palavra):
    status = False
    palavra = palavra.replace(' ','') #deixar sem espacos
    palavraInverso = palavra[::-1]
    if(palavra == palavraInverso):
        status = True
    
    return status


qtdLeituras = int(input())

for leituras in range(0, qtdLeituras):
    palavra = input().lower()
    
    resposta = 'NAO'
    if(serPalindromo(palavra)):
        resposta = 'SIM'
    print(resposta)
