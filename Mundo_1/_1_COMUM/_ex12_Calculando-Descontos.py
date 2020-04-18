preco= float(input("Qual o preço do produto?: R$"))
#produto com desconto de 5%
new_price= preco - (preco * 0.05)
print('\033[4;31m--- DESCONTO DE 5% em nossa loja!!! ---\033[m')
print('O preço do produto com \033[1;33m5%\033[m de desconto é \033[4;32mR${:.2f}'.format(new_price))