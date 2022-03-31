qtdMacacos = 0
pesoTrigres = 0
qtdCobrasBoludas = 0
cont = 0
while True:
    animal = input().lower()
    if(animal in 'macaco'):
        qtdMacacos += 1

    valorPeso = float(input())
    if(animal in 'tigre'):
        pesoTrigres += valorPeso
        cont += 1

    pais = input().lower()
    if(pais in 'venezuela' and animal in 'cobra'):
        qtdCobrasBoludas += 1
    
    prosseguir = input().upper()
    if(prosseguir in 'PARAR'):
        break

media = pesoTrigres / cont
print(qtdMacacos)
print('%.2f' %media)
print(qtdCobrasBoludas)