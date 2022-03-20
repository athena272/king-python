listaValores = input().split()
investimentoInicial = float(listaValores[0])
taxaJuros = float(listaValores[1])
periodoAnos = int(listaValores[2])

qtdLeituras = (periodoAnos * 12) // 3

for leituras in range(0, qtdLeituras):
    rendimento = investimentoInicial * taxaJuros
    montante = investimentoInicial + rendimento
    print("Rendimento: %.2f" %rendimento, "Montante: %.2f" %montante)

    investimentoInicial += rendimento