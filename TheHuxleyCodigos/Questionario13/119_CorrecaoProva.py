gabarito=input()
respostasdosalunos={}
notasalunos={}
ocorrenciasnotas={}
nota=0
notasacima6=0
listanotas=[]
while True:
    valores=input().split()
    codigoaluno=int(valores[0])
    if codigoaluno==9999:
        break 
    resposta=valores[1]
    respostasdosalunos[codigoaluno]=respostasdosalunos.get(codigoaluno,'')+resposta
for aluno in respostasdosalunos:
    for alternativa in range(10):
        if gabarito[alternativa]==respostasdosalunos[aluno][alternativa]:
            ponto=1.0
        else:
            ponto=0.0
        nota+=ponto
    notasalunos[aluno]=notasalunos.get(aluno,0)+nota 
    nota=0
for estudante in notasalunos:
    if notasalunos[estudante]>=6:
        notasacima6+=1
aprovados=(notasacima6/len(notasalunos))*100
for estudante in notasalunos:
    listanotas.append(notasalunos[estudante])
for nota in range(11):
    for resultado in listanotas:
        if nota ==resultado:
           ocorrenciasnotas[nota]=ocorrenciasnotas.get(nota,0)+1
for estudante in notasalunos:
    print(estudante,notasalunos[estudante])
print(str('%.1f'%aprovados)+'%')
print('%.1f'%max(ocorrenciasnotas,key=ocorrenciasnotas.get))