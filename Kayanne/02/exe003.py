listaIdade = list() #crio uma lista
listaNome = list() #crio uma lista
for i in range(0, 4):
    numPessoa = i + 1
    print(f"\n{numPessoa}º Pessoa\n")

    valorNome = str(input('Digite seu nome, por favor: ')).strip()

    valorIdade = int(input(f'Digite sua idade, por favor: '))

    listaNome.append(valorNome)

    listaIdade.append(valorIdade)
    
print("\nImprimindo pessoas com mais de 18 anos\n")    
pos = 0 #vai ajudar a encontrar a posicao do nome e da idade dentro da lista
for j in listaIdade:

    maiorIdade = (j >= 18)
    if maiorIdade:
        
        print(f"Nome: {listaNome[pos]}\n"
              f"Idade: {listaIdade[pos]}\n")

    pos = pos + 1

