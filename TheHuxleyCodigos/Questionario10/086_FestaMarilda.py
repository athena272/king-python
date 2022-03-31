def imprimirLinhas():
    print('--------------------------------------------------')
#Primeiro grupo de pessoas(lista inicial)
listNome = list()
while True:
    nome = input()
    if (nome.lower() == 'fim'):
        break
    listNome.append(nome)

#Mostrar lista inicial
listNome.sort()
for nomes in listNome:
    print(nomes)
imprimirLinhas()

#grupos de no maximo 5
while True:
    qtdLeituras = int(input())
    if(qtdLeituras == 0):
        break

    listConvidados = list()    
    cont = 0
    while cont < qtdLeituras:
        convidado = input()
        listConvidados.append(convidado)
        listConvidados.sort()
        cont += 1

    for convidados in listConvidados:
        print(convidados)
        imprimirLinhas()
