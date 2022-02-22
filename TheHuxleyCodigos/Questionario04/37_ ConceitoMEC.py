qtdLivros = int(input())
qtdAlunos = int(input())

livrosDisponiveis = qtdAlunos / qtdLivros

conceitoMEC = 'B'

if(livrosDisponiveis <= 8):
    conceitoMEC = 'A'
elif(livrosDisponiveis >= 13 and livrosDisponiveis <= 18):
    conceitoMEC = 'C'
elif(livrosDisponiveis > 18):
    conceitoMEC = 'D'

print(conceitoMEC)