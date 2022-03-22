nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

situacao = "Recuperacao"

if(media >= 7):
    situacao = "Aprovado"

elif(media < 5):
    situacao = "Reprovado"

print('Informe a primeira nota:')
print('Informe a segunda nota:')
print('Informe a terceira nota:')

print(situacao, 'com media %.1f' %media)