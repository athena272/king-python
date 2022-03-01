energiaConsumida = int(input())

#Encontrar o preco do KWh
precoKWh = 1.55

if(energiaConsumida <= 99):
    precoKWh = 1.35
elif(energiaConsumida >= 300 and energiaConsumida <= 574):
    precoKWh = 1.75
    energiaConsumida = energiaConsumida + (energiaConsumida * 0.1)#taxa de 10%, pois o consumo esta acima de 300
elif(energiaConsumida >= 575):
    precoKWh = 2.15
    energiaConsumida = energiaConsumida + (energiaConsumida * 0.1)#taxa de 10%, pois o consumo esta acima de 300
    
contaLuz = (energiaConsumida * precoKWh)

#menor valor da conta!
if(contaLuz < 35):
    contaLuz = 35

print('%.2f' %contaLuz)
print('%.2f' %precoKWh)
