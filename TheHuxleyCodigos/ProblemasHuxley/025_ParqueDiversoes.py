listaValores = input().split()

altura = int(listaValores[0])
idade = int(listaValores[1])

qtdBrinquedos = 0

if(altura >= 150 and idade >= 12):
    qtdBrinquedos += 1

if(altura >= 140 and idade >= 14):
    qtdBrinquedos += 1

if(altura >= 170 or idade >= 16):
    qtdBrinquedos += 1

print(qtdBrinquedos)