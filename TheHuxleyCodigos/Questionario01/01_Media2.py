#input de dados
notaA = float(input())
notaB = float(input())
notaC = float(input())

#Constantes
pesoA = 2 
pesoB = 3
pesoC = 5

media = ((notaA * pesoA) + (notaB * pesoB) + (notaC * pesoC)) / (pesoA + pesoB + pesoC)

print('MEDIA = %.1f' % media)