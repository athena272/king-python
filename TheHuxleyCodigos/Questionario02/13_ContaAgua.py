values = input().split()

qtdAgua = float(values[0]) * 1000 #pega o valor que esta em m³ e converte em litro direto
custoLitro = float(values[1])
 
contaAgua = (qtdAgua * custoLitro)
contaEsgoto = (contaAgua * 0.8)
contaTotal = contaEsgoto + contaAgua

print('%.2f' %contaAgua)
print('%.2f' %contaEsgoto)
print('%.2f' %contaTotal)

