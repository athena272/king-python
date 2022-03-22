day= int(input())
km= float(input())

diaria = 30 * day
kmPreco = 0.01 * km
porcento10 = (diaria + kmPreco) * 0.1
total = (diaria + kmPreco) - porcento10
print('%.2f' %total)
