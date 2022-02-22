#0 - mulher
#1 - homem
genero = int(input())
#0 - nao tem mais de 40
#1 - tem mais de 40
casaDos40 = int(input())
#1 caso fique barato

#0 caso fique caro
ehCaro = 0 #Comeco assumindo que sera caro

if(genero == 0 and casaDos40 == 1):
    ehCaro = 1#Nao fica caro, ou seja, barato

print(ehCaro)

