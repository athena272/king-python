from math import sqrt
#Guilherme
#valores = 4.06 + 4.58 + 5.05 = 13.69

#media = 13.69 / 3 = 4.56

#Cauan
#valores = 4.07 + 4.49 + 4.82 = 13.38

#media = 13.38 / 3 = 4.46

#Vitinho
#valores = 4.15 + 4.55 + 4.74 = 13.44

#media = 13.44 / 3 = 4.48

valoresInt = []
valores = input().split()
for valor in valores:
    valoresInt.append(float(valor))

somaValor = sum(valoresInt)

media = somaValor / 3

desvioPadrao = sqrt(((valoresInt[0] - media) ** 2 + (valoresInt[1] - media)  ** 2 + (valoresInt[2] - media) ** 2) / 2)

incertezaA = desvioPadrao / sqrt(3)

print('Incerteza t: %.2fs' % incertezaA)
#letraB
incertezaPeriodo = sqrt((1/5) ** 2 * incertezaA ** 2)

print('Incerteza T: %.2fs' %incertezaPeriodo)

valorPeriodoT = media / 5

print('O valor do periodo T:', '%.2fs' % valorPeriodoT)
