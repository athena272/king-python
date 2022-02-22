quantiaSacar = int(input())

print(quantiaSacar)
#Contar qtd de cedulas e ir diminuindo o quanto falta ser sacado
qtdCedulas100 = (quantiaSacar // 100) #qtd de cedulas de 100 reais usadas 
quantiaSacar = (quantiaSacar % 100) #Atualiza o valor da quantia restante
print(qtdCedulas100,'nota(s) de R$ 100,00')

qtdCedulas50 = (quantiaSacar // 50) #qtd de cedulas de 50 reais usadas
quantiaSacar = (quantiaSacar % 50) #Atualiza o valor da quantia restante
print(qtdCedulas50,'nota(s) de R$ 50,00')

qtdCedulas20 = (quantiaSacar // 20) #qtd de cedulas de 20 reais usadas
quantiaSacar = (quantiaSacar % 20) #Atualiza o valor da quantia restante 
print(qtdCedulas20,'nota(s) de R$ 20,00')

qtdCedulas10 = (quantiaSacar // 10) #qtd de cedulas de 10 reais usadas
quantiaSacar = (quantiaSacar % 10) #Atualiza o valor da quantia restante
print(qtdCedulas10,'nota(s) de R$ 10,00')

qtdCedulas5 = (quantiaSacar // 5) #qtd de cedulas de 5 reais usadas
quantiaSacar = (quantiaSacar % 5) #Atualiza o valor da quantia restante
print(qtdCedulas5,'nota(s) de R$ 5,00')

qtdCedulas2 = (quantiaSacar // 2) #qtd de cedulas de 2 reais usadas
quantiaSacar = (quantiaSacar % 2) #Atualiza o valor da quantia restante
print(qtdCedulas2,'nota(s) de R$ 2,00')

qtdCedulas1 = (quantiaSacar // 1) #qtd de cedulas de 1 reais usadas
quantiaSacar = (quantiaSacar % 1) #Atualiza o valor da quantia restante
print(qtdCedulas1,'nota(s) de R$ 1,00')











