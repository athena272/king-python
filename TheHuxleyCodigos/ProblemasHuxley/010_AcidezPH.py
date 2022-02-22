ph = float(input())

solucao = 'Neutra'

if(ph < 7):
    solucao = 'Acida'
elif(ph > 7):
    solucao = 'Basica'

print(solucao)