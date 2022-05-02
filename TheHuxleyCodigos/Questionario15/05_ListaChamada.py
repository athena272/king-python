listaValores = input().split()
qtdLeituras = int(listaValores[0])
posVencedor = int(listaValores[1])

listaAlunos = list()
for i in range(qtdLeituras):
    nomeAluno = input()
    listaAlunos.append(nomeAluno)
listaAlunos.sort()

vencedor = listaAlunos[posVencedor - 1]
print(vencedor)
