tamanho = int(input())
via = []
resultado = "OK"


def passagem(linhaAntes, linhaDepois):
    for i in range(tamanho):
        if linhaAntes[i] == 1 and linhaDepois[i] == 1:
            return True
        else:
            pass
    return False


for i in range(tamanho):
    matriz = [int(elemento) for elemento in input().split()]
    via.append(matriz)

for i in range(tamanho):
    if i+1 != tamanho:
        if passagem(via[i], via[i+1]) and via[0][0] == 1 and via[tamanho-1][tamanho-1] == 1:
            continue
        else:
            resultado = "NOT OK"
            break
    else:
        break

print(resultado)

