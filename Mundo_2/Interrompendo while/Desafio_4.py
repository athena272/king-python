num_pessoa = 1
idade_18 = 0
cadastro_homem = 0
mulheres_menor_20 = 0
while True:
    print(f'=== CADASTRO {num_pessoa}ª PESSOA ===')
    print('------------------------------------')
    idade = int(input('Digite sua idade: '))
    if (idade > 18):
        idade_18 += 1
    sex = str(input('Seu sexo [M / F]: ')).strip().upper()[0]
    while sex not in 'MF':
        sex = str(input('Seu sexo [M / F]: ')).strip().upper()[0]
    if (sex == 'M'):
        cadastro_homem += 1
    if (sex == 'F' and idade < 20 ):
        mulheres_menor_20 += 1
    print('-------------------------------------')
    pergunta = str(input('Quer continuar? [s / n]: ')).strip().lower()[0]
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar? [s / n]: ')).strip().lower()[0]
    if (pergunta == 'n'):
        break
    print('--------------------------------------')
    num_pessoa += 1
print('==== FIM PROGRAMA ===')
print('\n'
      f'Total de pessoas com mais de 18: {idade_18} pessoas'
      f'\nExistem {cadastro_homem} homens cadastrados'
      f'\ne temos {mulheres_menor_20} mulher(es) com menos de 20 anos')