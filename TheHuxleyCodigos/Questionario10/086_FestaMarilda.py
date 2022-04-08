def imprimirLinhas():
    print('--------------------------------------------------')
#Primeiro grupo de pessoas(lista inicial)
listNome = list()
while True:
    nome = input()
    if (nome.lower() == 'fim'):
        break
    listNome.append(nome)

#grupos de no maximo 5
while True:
    #Exibir nomes até o momento
    listNome.sort()
    for convidados in listNome:
            print(convidados)
    imprimirLinhas()

    qtdLeituras = int(input())
    if(qtdLeituras == 0):
        break

    cont = 0
    while cont < qtdLeituras:
        
        convidado = input()
        listNome.append(convidado)
        cont += 1

    