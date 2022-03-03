#declaracao de funcoes
def AnalisarSituacao(nota1, nota2, nota3, nota4):
    peso1 = 1
    peso2 = 2
    peso3 = 3
    peso4 = 4
    media = (nota1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / (peso1 + peso2 + peso3 + peso4)
    situacao = "prova final"
    
    if (media >= 9):
        situacao = "aprovado com louvor"
    elif (media >= 7):
        situacao = "aprovado"
    elif (media < 3):
        situacao = "reprovado"
        
    return situacao

    
#entrada de dados
listaValores = input().split()

nota1 = float(listaValores[0])
nota2 = float(listaValores[1])
nota3 = float(listaValores[2])
nota4 = float(listaValores[3])


print(AnalisarSituacao(nota1, nota2, nota3, nota4))