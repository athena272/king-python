listaValores = input().split()
limiteInferior = int(listaValores[0])
limiteSuperior = int(listaValores[1])

texto = ''
for comeco in range(limiteInferior, limiteSuperior + 1):
    multiplo5 = (comeco % 5 == 0)
    if(multiplo5):
        texto += str(comeco) + '|'

ultimaPos = len(texto) - 1 #Tirar a barra do final
print(texto[0:ultimaPos])
