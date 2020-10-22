pound = float(input("Qual seu peso?(KG): "))
high = float(input("Qual sua altura?(m): "))

IMC = pound / (high ** 2)
print("O Seu IMC é {:.2f}".format(IMC))
if (IMC < 18.5):
    print("Você está ABAIXO do peso!")
elif (18.5 < IMC <= 24.9):
    print("Você está com peso normal!")
elif (24.9 < IMC <= 29.9):
    print("Você com SobrePeso!")
elif (29.9 < IMC <= 39.9):
    print("Você está com OBESIDADE")
elif (IMC >= 40):
    print("Você está com OBESIDADE MÓRBIDA")



