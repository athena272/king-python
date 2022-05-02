listaValores = input().split()
qtdLinhas = int(listaValores[0])
qtdColunas = int(listaValores[1])
maior = [1]
matriz = []
for _ in range(qtdLinhas):
    elemento = [int(elem) for elem in input().split()][0:qtdColunas]
    matriz.append(elemento)

i = 0
for linha in matriz:
    seq=1
    sequen = [1]
   
    for elem in range(len(linha)-1):
        if linha[elem] <= linha[elem+1]:
            seq+=1
        sequen.append(seq)
        maior.append(seq)
        if linha[elem] > linha[elem+1]:
            seq = 1
    
    print("Linha",str(i)+":",max(sequen))
    i+=1

print("Maior Sequencia:", max(maior))