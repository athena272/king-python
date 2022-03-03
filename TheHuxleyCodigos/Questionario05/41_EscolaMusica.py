#declaracao de funcoes
def ClassificaAluno(media, faltas):
    situacao = "APROVADO"
    
    if (media >= 9.5 and faltas <= 10):
        situacao = "APROVADO COM LOUVOR"
    elif(faltas > 10):
        situacao = "REPROVADO POR FALTAS"
    if (media < 7):
        situacao = "REPROVADO"

    return situacao

#entrada de dados
mediaAluno = float(input())
qtdFaltas = int(input())

print(ClassificaAluno(mediaAluno, qtdFaltas))
