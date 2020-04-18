from random import choice
name1= str(input('Nome do primeiro aluno: '))
name2= str(input('Nome do segundo aluno: '))
name3= str(input('Nome do terceiro aluno: '))
name4= str(input('Nome do quarto aluno: '))
nomes= [name1, name2, name3, name4]
sortear= choice(nomes)
print('O nome escolhido foi {} '.format(sortear))