from math import sqrt, ceil, floor

#1

#Opcao A
# volume = (1/3) * 9.59 * (3.42 ** 2)

# print(volume)

# densidade = 101 / volume

# print(densidade)

# #Opcao B
# erroRelativo = ((densidade - 2.7) / 2.7) * 100

# print(erroRelativo)

#2

def Mm (lista):
    soma = 0
    for index in range(len(lista)):
        soma = soma + lista[index]
    return soma/ len(lista)

def dpm(lista):
    somatorio = 0
    for index in range(len(lista)):
        somatorio = somatorio + (lista[index] - Mm(lista))**2
    return sqrt( somatorio/ (len(lista)-1)  )

# Opcao A

# diametroBaseMedia = [3.75, 3.50, 3.8]

# resultadoBaseMedia = dpm(diametroBaseMedia) / sqrt(3)

# print(resultadoBaseMedia)

# alturaCilindro = [9.40, 9.40, 9.45]

# resultadoAlturaCilindro = dpm(alturaCilindro) / sqrt(3)

# print(resultadoAlturaCilindro)

#Opcao B
# mediaDiametro = (3.75 + 3.50 + 3.8) / 3

# print(mediaDiametro)

# mediaAltura = (9.40 + 9.40 + 9.45) / 3

# print(mediaAltura)

#3

#lei Hooke | F = -kdeltaX
            #  3 = -k0.09m    

#Opcao A

# constaElastica1 =  -1 * (3 /0.09)

# print(constaElastica1)

# # Opcao B

# distanciaMola = (0.09 * 3.5)

# constaElastica = -1 * (3 / distanciaMola)

# print(constaElastica)

#4

#Opcao A

# mediaL = (18.6 + 18.85 + 20.5 + 19.90 + 18.55 + 20.15 + 19.0) / 7

# mediaR = (6.4 + 6.4 + 6.10 + 6.55 + 6.85 + 6 + 6.55) / 7

# print(mediaL)
# print(mediaR)

# # #Opcao B

# pi = 3.14159265359
# raio = mediaR
# larg = mediaL

# al = pi*raio*larg+2*raio*larg
# at = al+ pi*raio**2

# print(at)



