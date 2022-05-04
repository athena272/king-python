casos = int(input())

cpfLista = [ int(input()) for _ in range(casos)]
notaLista = [ int(input()) for _ in range(casos)]


def buscaBinaria(lista, chave):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim)//2
        if lista[meio] == chave:
            return meio
        elif lista[meio] > chave:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

casosTeste = int(input())
for _ in range(casosTeste):
    cpf = int(input())
    posicao = buscaBinaria(cpfLista,cpf)
    if posicao >= 0:
        print(notaLista[posicao])
    else:
        print("NAO SE APRESENTOU")