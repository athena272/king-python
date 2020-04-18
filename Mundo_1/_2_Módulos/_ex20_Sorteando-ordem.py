from random import shuffle
name1 = str(input('Nome do primeiro aluno: '))
name2 = str(input('Nome do segundo aluno: '))
name3 = str(input('Nome do terceiro aluno: '))
name4 = str(input('Nome do quarto aluno: '))
lista= [name4, name3, name2, name1]
shuffle(lista)
print('A nova ordem de apresentação será:'
      '\n{}'.format(lista))