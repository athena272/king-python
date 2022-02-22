quantiaSacar = int(input())
#cedulas de 100, 50, 20, 10, 5, 2 e 1. 
maiorCedula = 100
qtdCedula = 0

print(quantiaSacar)

while True:
    if(quantiaSacar >= maiorCedula): #Se eu poder tirar aquela cedula
        quantiaSacar -= maiorCedula #ir sacando o valor da maior cedula atual do montante total
        qtdCedula += 1 #contar quantas cedulas foram usadas
    else: #Se eu nao consigo mais tirar, eh hora de mudar a maior cedula atual
        print(str(qtdCedula) + ' nota(s) de R$ ' + str(maiorCedula) + ',00')
        #Cascata de elif's para trocar a cedula usada para
        if(maiorCedula == 100):
            maiorCedula = 50
        elif(maiorCedula == 50):
            maiorCedula = 20
        elif(maiorCedula == 20):
            maiorCedula = 10
        elif(maiorCedula == 10):
            maiorCedula = 5
        elif(maiorCedula == 5):
            maiorCedula = 2
        elif(maiorCedula == 2):
            maiorCedula = 1
        #Se o dinheiro para sacar for totalmente retirado, eh hora de acabar
        elif(quantiaSacar == 0):
            break;

        qtdCedula = 0 #Sempre que trocar a cedula usada, eu reinicio a contagem

       





