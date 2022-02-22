qtdDias = int(input())
kmRodados = int(input())

diaria = 90 * qtdDias
kmDiaria = 100 * qtdDias
kmExtras = 0

if(kmRodados > kmDiaria): #Se a pessoa andou mais do que 100km por dia
    kmExtras = (kmRodados - kmDiaria) * 12 #encontro os km extras e calculo a taxa

totalPago = diaria + kmExtras

print('%.2f' % totalPago)