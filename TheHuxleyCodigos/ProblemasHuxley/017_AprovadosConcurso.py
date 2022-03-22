# O IBGE realizou um concurso para contratar pessoas para trabalhar no censo. Cada candidato fez uma prova de português com 50 questões, outra de matemática com 35 questões, e uma prova de redação.

# Para ser aprovado, era necessário acertar pelo menos 80% da prova de português, 60% da prova de matemática, e ter nota igual ou superior a 7 na redaçã
def serAprovado(portugues, matematica, redacao):
    situacao = False
    if(portugues >= 40 and matematica >= 21 and redacao >= 7):
        situacao = True
    
    return situacao


qtdAprovados = 0
while True:
    notaPortuguese = int(input())
    if(notaPortuguese < 0):
        break
    
    notaMatematica = int(input())
    notaRedacao = float(input())
    if(serAprovado(notaPortuguese, notaMatematica, notaRedacao)):
        qtdAprovados += 1
    
print(qtdAprovados)
