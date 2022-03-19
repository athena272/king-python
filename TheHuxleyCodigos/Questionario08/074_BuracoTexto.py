qtdLeituras = int(input())

cont = 0
qtdBuracos = 0
while cont < qtdLeituras:
    palavra = input().upper()
    for letra in palavra:
        if(letra in 'ADOPRQ'):
            qtdBuracos += 1
        elif(letra in 'B'):
            qtdBuracos += 2

    print(qtdBuracos)
    qtdBuracos = 0 #Resetar contador de buracos

    cont += 1


    