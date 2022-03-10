def valorDiariaCategoria(categoria, diaria):
    diariaCategoria = 100
    if(categoria == 'S'):
        diariaCategoria = 150
    elif(categoria == 'X'):
        diariaCategoria = 200
    elif(categoria == 'U'):
        diariaCategoria = 300
           
    return (diariaCategoria * diaria)

def valorKm(categoria, kmPercorridos):
    precoKm = 0.5 * kmPercorridos
    if(categoria == 'X'):
        precoKm = 0.8 * kmPercorridos
    elif(categoria == 'U'):
        precoKm = 1 * kmPercorridos
    
    return precoKm

def valorDesconto(fidelidade):
    desconto = 0.05 #Desconto de 5 porcento
    if(fidelidade == 'platinum'):
        desconto = 0.1 #Desconto de 10 porcento
    elif(fidelidade == 'infinity'):
        desconto = 0.2 #Desconto de 20 porcento
    
    return desconto

    
def calcular_tarifa(categoria, kmPercorridos, diaria, fidelidade):
    diariaCategoria = valorDiariaCategoria(categoria, diaria) 
    custoKm = valorKm(categoria, kmPercorridos)
    descontoFidelidade = (diariaCategoria + custoKm) * valorDesconto(fidelidade)
    totalPagar = (diariaCategoria + custoKm) - descontoFidelidade

    return totalPagar
    
categoria = input()
kmPercorridos = int(input())
diaria = int(input())
fidelidade = input()

pagarTotal = calcular_tarifa(categoria, kmPercorridos, diaria, fidelidade)

print('%.2f' %pagarTotal)