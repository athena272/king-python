academia = {}

while True:
    nome = input()
    if nome == "SAIR":
        break
    senha = int(input())
    mensalidade = input()
    academia[nome] = (senha,mensalidade)

while True:
    senha = int(input())
    if senha == -1:
        break
    for nome,valor in academia.items():

        senhaBate = 0
        pago = 0
        if valor[0] == senha and valor[1] != 'P':
            pago = 0
            senhaBate = 1
            break
        elif valor[0] == senha and valor[1] == 'P':
            pago = 1
            senhaBate = 1
            break
    if pago == 0 and senhaBate == 1:
        print("Nao esta esquecendo de algo,",nome+"? Procure a recepecao!")
    elif pago == 1 and senhaBate == 1:
        print(nome+", seja bem-vindo(a)!")
    else:
        print("Seja bem-vindo(a)! Procure a recepecao!")