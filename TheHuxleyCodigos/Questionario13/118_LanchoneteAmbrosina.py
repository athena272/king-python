numerodeprodutos=int(input())
precos={}
codigos={}
listacodigos=[]
pagamento=0
for elemento in range(numerodeprodutos):
    codigo=int(input())
    nomeproduto=input()
    preco=float(input())
    precos[nomeproduto]=precos.get(nomeproduto,0)+preco 
    codigos[codigo]=codigos.get(codigo,'')+nomeproduto
    listacodigos.append(codigo)
while True:
    codigopedido=int(input())
    if codigopedido==0:
        break
    numerointens=int(input())
    if codigopedido not in listacodigos:
        precoTotalProduto=0
    else:
        if numerointens<0:
            precoTotalProduto=0
        else:
            produtoescolhido=codigos[codigopedido]
            precoTotalProduto=precos[produtoescolhido]*numerointens
    pagamento+=precoTotalProduto
print('%.2f'%pagamento)