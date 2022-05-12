palpites={}
chutes=int(input())
listachute=[]
listaparticipantes=[]
for chut in range(chutes):
    escolhas=input().split()
    for escolha in escolhas:
        listachute.append(escolha)
    listachute.pop(0)
    palpites[escolhas[0]]=listachute[::]
    listachute.clear()
    listaparticipantes.append(escolhas[0])
while True:
    presenteRecebido=input().split()
    if presenteRecebido[0]=='FIM':
        break
    if presenteRecebido[0] not in listaparticipantes:
        print('Tente Novamente!')
    else:
        if presenteRecebido[1] not in palpites[presenteRecebido[0]]:
            print('Tente Novamente!')
        else:
            print('Uhul! Seu amigo secreto vai adorar')