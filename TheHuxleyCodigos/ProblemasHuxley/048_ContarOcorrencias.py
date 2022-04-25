def contarOcorrencia(caracter, listaPalavras):
    ocorrencia = 0
    for palavra in listaPalavras:
        ocorrencia += palavra.count(caracter)

    return ocorrencia

qtdLeituras = int(input())

listaPalavras = list()
for i in range(0, qtdLeituras):
    palavra = input()
    listaPalavras.append(palavra)

buscar = input()

for caracter in buscar:
    print(caracter, '=', contarOcorrencia(caracter, listaPalavras))