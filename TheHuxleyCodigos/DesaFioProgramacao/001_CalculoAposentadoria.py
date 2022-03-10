def podeAposentar(idade, tempoTrabalho):
    aposentado = False
    if(idade >= 65 and tempoTrabalho >= 5):
        aposentado = True
    elif(tempoTrabalho >= 30):
        aposentado = True
    elif(idade >= 60 and tempoTrabalho >= 25):
        aposentado = True

    return aposentado
    

def tempoAposentar(idade, tempoTrabalho):
    tempoAposentar = 0
    if(idade >= 65 or idade > 60):
        tempoAposentar = 5 - tempoTrabalho
    elif(idade >= 60):
        tempoAposentar = 25 - tempoTrabalho
    else:
        tempoAposentar = 30 - tempoTrabalho

    return tempoAposentar


#input de dados
listaValores = input().split()
idade = int(listaValores[0])
tempoTrabalho = int(listaValores[1])
#Retorno caso possa se aposentar
if(podeAposentar(idade, tempoTrabalho)):
    print('Pode se aposentar')
#Caso nao possa, verifica quanto tempo falta
else:
    tempoRestante = tempoAposentar(idade, tempoTrabalho)
    if(tempoRestante == 1):
        print('Não pode se aposentar: Ainda falta',  tempoRestante,'ano de trabalho')
    else:
        print('Não pode se aposentar: Ainda faltam',  tempoRestante,'anos de trabalho')