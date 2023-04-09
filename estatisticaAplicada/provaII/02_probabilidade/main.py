# Importando a biblioteca random para simular a retirada das cartas
import random

# Total de cartas no baralho
total_cartas = 52

# Total de áses no baralho
total_ases = 4

# Total de cartas de copas no baralho
total_copas = 13

# Simulando a retirada das cartas
primeira_carta = random.randint(1, total_cartas) # Retirando a primeira carta
total_cartas -= 1 # Atualizando o total de cartas restantes
segunda_carta = random.randint(1, total_cartas) # Retirando a segunda carta

# Verificando se a primeira carta é um ás e a segunda carta é uma carta de copas
if primeira_carta <= total_ases and segunda_carta <= total_copas:
    # Se a condição for satisfeita, significa que tiramos um ás e uma carta de copas
    probabilidade = 1 / total_cartas
else:
    probabilidade = 0

print("A probabilidade de tirar um ás e, em seguida, tirar uma carta de copas é:", probabilidade)

# Importando a biblioteca random para simular a retirada das cartas
import random

# Total de bolas na urna
total_bolas = 4 + 3 + 5

# Total de bolas vermelhas na urna
total_vermelhas = 4

# Simulando a retirada das bolas
primeira_bola = random.randint(1, total_bolas) # Retirando a primeira bola
total_bolas -= 1 # Atualizando o total de bolas restantes
segunda_bola = random.randint(1, total_bolas) # Retirando a segunda bola

# Verificando se ambas as bolas retiradas são vermelhas
if primeira_bola <= total_vermelhas and segunda_bola <= total_vermelhas - 1:
    # Se a condição for satisfeita, significa que ambas as bolas são vermelhas
    probabilidade = 1 / total_bolas
else:
    probabilidade = 0

print("A probabilidade de retirar duas bolas vermelhas consecutivamente e sem reposição é:", probabilidade)

# Importando a biblioteca random para simular a retirada das cartas
import random

# Total de alunos na turma
total_alunos = 30

# Total de alunos que gostam de Matemática
total_matematica = 15

# Total de alunos que gostam de Física
total_fisica = 20

# Calculando a probabilidade de gostar de Matemática ou Física
probabilidade = (total_matematica + total_fisica) / total_alunos

print("A probabilidade de um aluno gostar de Matemática ou Física é:", probabilidade)

# Importando a biblioteca random para simular o lançamento do dado
import random

# Total de faces do dado
total_faces = 6

# Simulando o lançamento do dado
resultado = random.randint(1, total_faces) # Lançando o dado

# Verificando se o resultado é um número par ou maior que 4
if resultado % 2 == 0 or resultado > 4:
    # Se a condição for satisfeita, significa que obtemos um número par ou um número maior que 4
    probabilidade = 1 / total_faces
else:
    probabilidade = 0

print("A probabilidade de obter um número par ou um número maior que 4 em um único lançamento de dado é:", probabilidade)

# Importando a biblioteca random para simular o lançamento do dado
import random

# Total de bolas na caixa
total_bolas = 6 + 4

# Total de bolas vermelhas na caixa
total_vermelhas = 6

# Simulando a retirada das bolas
primeira_bola = random.randint(1, total_bolas) # Retirando a primeira bola
segunda_bola = random.randint(1, total_bolas) # Retirando a segunda bola
terceira_bola = random.randint(1, total_bolas) # Retirando a terceira bola

# Verificando se todas as bolas retiradas são vermelhas
if primeira_bola <= total_vermelhas and segunda_bola <= total_vermelhas and terceira_bola <= total_vermelhas:
    # Se a condição for satisfeita, significa que todas as bolas são vermelhas
    probabilidade = 1 / (total_bolas ** 3)
else:
    probabilidade = 0

print("A probabilidade de retirar três bolas vermelhas consecutivamente com reposição é:", probabilidade)

