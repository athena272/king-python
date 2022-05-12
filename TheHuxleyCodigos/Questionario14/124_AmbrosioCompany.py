ambrosio = {}
while True:
    numPassagem = int(input())
    if numPassagem == -1:
        break
    data = input()
    de = input()
    para = input()
    horario = input()
    poltrona = int(input())
    idade = int(input())
    nome = input()
    ambrosio[nome] = (idade,numPassagem,data,de,para,horario,poltrona)

lista = list(ambrosio.values())
mediaIdade = sum([elem[0] for elem in lista])//len(lista)

for nome,caracteristicas in ambrosio.items():
    if caracteristicas[0] > mediaIdade and caracteristicas[-1] % 2 == 0:
        print(nome)