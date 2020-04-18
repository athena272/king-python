words= 'G2 Superior a todos'
#analisando string
print(len(words))# Ler o número de posições, "comprimento"
print('')

print(words.count('o'))#contar quantas vezes aparece a letra "o"
print('')
#words.count('o',0,13) Já vem com fatiamento imcluso
print(words.find('ior'))#indica a posição em que começa a palavra caçada
print('')
print(words.find('Alicia'))#letras que não existem na cadeia de caracteres
#sai resultado -1
print('')
print('Superior' in words)#Retorna um valor lógico, se existe or not a palavra na string
print('')
print(words.replace('Superior','Inferior'))#Replace == Troca; troca a parte desejada, por outra série de caracteres
print('')
print(words.upper())#deixa todos caracteres em Caixa Alta
print('')
print(words.lower())#deixa todos caracteres em Caixa Baixa
print('')
print(words.capitalize())#só primeiro fica maisculo
print('')
print(words.title())#analisa e coloca todas as palavras em Capatalize
print('')
print(words.strip())#remove espaços inúteis antes e depois da string
print('')
print(words.rstrip())#remove espaços inúteis à direita 'r'; right == direita
print('')
print(words.lstrip())#remove espaços inúteis à esquerda 'l '; lefth == esquerda
print('')
print(words.split())#recorta a lista
print('')
print('|'.join(words))#junta a string com algum separador