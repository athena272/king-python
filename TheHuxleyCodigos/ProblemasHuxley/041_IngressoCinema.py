precoIngresso = float(input())
categoria = input().upper()

valorPagar = precoIngresso
if(categoria == 'E'):
    valorPagar *= 0.5
    print('Preco com desconto: R$%.2f' %valorPagar)
    print('Categoria: Estudante')
elif(categoria == 'A'):
    valorPagar -= (valorPagar * 0.3)
    print('Preco com desconto: R$%.2f' %valorPagar)
    print('Categoria: Aposentado')
elif(categoria == 'N'):
    print('Preco sem desconto: R$%.2f' %valorPagar)
else:
    print('Categoria invalida!')