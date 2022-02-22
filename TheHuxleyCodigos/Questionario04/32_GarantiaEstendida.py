precoProduto = float(input())
anosGarantia = int(input())

if(anosGarantia == 1): #A garantia de 1 ano, custa 3% do produto
    precoProduto = precoProduto + (precoProduto * 0.03)
elif(anosGarantia == 2): #A garantia de 2 anos, custa 5% do produto
    precoProduto = precoProduto + (precoProduto * 0.05)

print('%.2f' %precoProduto)