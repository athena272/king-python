nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

situacao = "prova final"

if(media >= 7):
    situacao = "aprovado"

elif(media < 3):
    situacao = "reprovado"

print(situacao)