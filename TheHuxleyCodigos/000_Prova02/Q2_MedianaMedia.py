def calcMediana(listaNum):
    pos = (len(listaNum) - 1) // 2
    mediana = listaNum[pos]
    
    if(len(listaNum) % 2 == 0):
        pos = len(listaNum) // 2
        valor1 = listaNum[pos]
        valor2 = listaNum[pos - 1]
        mediana = (valor1 + valor2) / 2

    return mediana


listaMedia = list()
while True:
    valores = input()
    #Nao coloquei o break para interrromper o laco
    if(valores == '*'):
        break

    #so eh necessario e so faz sentido dar apenas um split, com base na virgula
    valores = valores.split(',')
    #a conversao eh para float(), nao para int()
    valores = [float(i) for i in valores]
    
    media = sum(valores) / len(valores)
    listaMedia.append(media)

texto = ''
for num in listaMedia:
    texto += str('%.2f' %num) + ' '

texto = ' '.join(texto.split())
print(texto)

listaMedia.sort(reverse=True)

textoSaida = ''
for numMedia in listaMedia:
    textoSaida += str('%.2f' %numMedia) + ' '

textoSaida = ' '.join(textoSaida.split())
print(textoSaida)

mediana = calcMediana(listaMedia)
print('Mediana das medias: %.2f' %mediana)