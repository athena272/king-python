def retirarConsoantes(msg):
    palavraSemVogais = ''
    for letra in msg:
        if(letra in 'aeiou'):
            palavraSemVogais += letra
    
    return palavraSemVogais


def soConsoante(msg):
    status = True
    for letra in msg:
        if(letra in 'aeiou'):
            status = False
            break
    
    return status

def serPalindromo(palavra):
    status = False
    palavra = palavra.replace(' ','') #deixar sem espacos
    palavraInverso = palavra[::-1]
    if(palavra == palavraInverso):
        status = True
    
    return status

def textoEngracado(msg):
    status = False
    vogaisTexto = retirarConsoantes(msg)
    if(serPalindromo(vogaisTexto)):
        status = True
    
    return status


qtdLeituras = int(input())

cont = 0
while cont < qtdLeituras:
    textoRisada = input().lower()
    
    if(soConsoante(textoRisada) or len(textoRisada) > 50):
        print('INVALIDA')
        cont += 1
        continue

    if(textoEngracado(textoRisada)):
        print('ENGRACADA')
    
    else:
        print('SEM GRACA')


    cont += 1