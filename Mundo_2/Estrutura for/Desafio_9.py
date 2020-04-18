from datetime import date
maiores_idade = 0
menores_idade = 0
data_atual = date.today()
for i in range(1, 8):
    age = int(input('olá, qual seu ano de nascimento, por favor: '))
    idade = (data_atual.year - age)
    if (idade >= 21):
        maiores_idade += 1
    else:
        menores_idade += 1
print('Existem {} pessoas com 21 anos ou mais'
      '\ne {} pessoas com menos de 21 anos'.format(maiores_idade, menores_idade))