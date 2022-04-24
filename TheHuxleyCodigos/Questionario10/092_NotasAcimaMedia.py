qtdLeituras = int(input())

listaNotas = list()
for leitura in range(0, qtdLeituras):
    nota = float(input())
    listaNotas.append(nota)

mediaNotas = sum(listaNotas) / len(listaNotas)
acimaMediaVariacao = mediaNotas + (mediaNotas * 0.1)
baixoMediaVariacao = mediaNotas - (mediaNotas * 0.1)

qtdAcimaMedia = 0
qtdAbaixoMedia = 0
for nota in listaNotas:
    if(nota > acimaMediaVariacao):
        qtdAcimaMedia += 1
    if(nota < baixoMediaVariacao):
        qtdAbaixoMedia += 1

print('%.2f' %mediaNotas)
print(qtdAcimaMedia)
print(qtdAbaixoMedia)

