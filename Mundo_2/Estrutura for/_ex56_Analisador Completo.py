media = 0
homem_mais_velho = 0
nome_homem_velho = ''
mulheres_menor_20_anos = 0
for i in range(1, 5):
    print('--- {}ª PESSOA ---'.format(i))
    name = str(input('Digite aqui, seu nome, por favor: ')).capitalize()
    age = int(input('Qual sua idade, por favor: '))
    sex = str(input('Qual seu sexo, por favor [F / M]: ')).upper()
    media += age #valores das idades de todo o grupo
    if (sex == 'F') and (age < 20): #mulhres com menos de 20 anos
        mulheres_menor_20_anos += 1
    if (i == 1):
        homem_mais_velho = age
        nome_homem_velho = name
    else:
        if (homem_mais_velho < age):
            homem_mais_velho = age
            nome_homem_velho = name
media_final = media / i
print('---------RESULTADOS-----------'
      '\nA média das idades do grupo é de {} anos'
      '\nO Homem mais velho tem {} anos e seu nome é {}'
      '\nExistem {} mulheres com menos de 20 anos'.format(media_final, homem_mais_velho, nome_homem_velho, mulheres_menor_20_anos))