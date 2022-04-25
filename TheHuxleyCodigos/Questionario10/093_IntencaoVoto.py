def   vantagem(candidato, concorrente, qtdVotos):
    listaVantagens = [0.00]
    for posVoto in range(0, qtdVotos):
        if candidato[posVoto] > concorrente[posVoto]:
            tirarVantagem = float(candidato[posVoto]) - float(concorrente[posVoto])
            listaVantagens.append(tirarVantagem)

    return max(listaVantagens)

qtdVotos = int(input())
candidato = input().split()
concorrente = input().split()

maiorVantagem = vantagem(candidato, concorrente, qtdVotos)
print("%.2f" %maiorVantagem)
