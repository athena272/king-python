valores = []
mulhervfl = 0
while True:
        idade = int(input())
        if idade == -1:
            break
        sexo,cabelo,olhos = input().split()
        valores.append((idade,sexo,olhos,cabelo))


maximoIdade = max(valores)[0]
print("Mais velho:",maximoIdade)
for (idade,sexo,olhos,cabelo) in valores:
    if idade <= 35 and idade >= 18 and olhos == "v" and sexo == "f" and cabelo == "l":
        mulhervfl +=1
percentual = "%.2f"%(mulhervfl/len(valores)*100)
print("Mulheres com olhos verdes, loiras com 18 a 35 anos:",str(percentual)+"%")