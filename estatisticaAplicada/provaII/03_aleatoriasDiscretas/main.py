# Dicionário com o número de irmãos e a quantidade de alunos para cada quantidade de irmãos
dados = {0: 12, 1: 8, 2: 5, 3: 3, 4: 1, 5: 1}

# Total de alunos na sala de aula
total_alunos = 30

# Calculando a probabilidade de ter pelo menos um irmão
probabilidade = sum(dados.values()) / total_alunos

print("A probabilidade de um aluno ter pelo menos um irmão é:", probabilidade)

# Importando a biblioteca random para simular o embaralhamento do baralho
import random

# Total de cartas no baralho
total_cartas = 52

# Total de cartas de ouros no baralho
total_ouros = 13

# Simulando a retirada de uma carta
carta = random.randint(1, total_cartas) # Retirando uma carta

# Verificando se a carta retirada é de ouros
if carta <= total_ouros:
    # Se a carta for de ouros, significa que obtemos uma carta de ouros
    probabilidade = 1 / total_cartas
else:
    probabilidade = 0

print("A probabilidade de obter uma carta de ouros é:", probabilidade)

# Total de faces do dado
total_faces = 6

# Probabilidade de obter um número ímpar em um único lançamento
probabilidade_impares = 3 / total_faces

# Inicializando o número esperado de lançamentos necessários
numero_esperado_lancamentos = 0

# Probabilidade de não obter um número ímpar em um único lançamento
probabilidade_nao_impares = 1 - probabilidade_impares

# Loop para calcular o número esperado de lançamentos necessários
while True:
    numero_esperado_lancamentos += 1
    probabilidade_todos_nao_impares = probabilidade_nao_impares ** numero_esperado_lancamentos
    if probabilidade_todos_nao_impares < 0.5:
        break

print("O número esperado de lançamentos necessários para obter um número ímpar é:", numero_esperado_lancamentos)


# Probabilidade de comprar uma camiseta
probabilidade_camiseta = 0.3

# Probabilidade de comprar uma calça
probabilidade_calca = 0.4

# Probabilidade de comprar uma blusa
probabilidade_blusa = 0.2

# Calculando a probabilidade de comprar uma camiseta ou uma calça
probabilidade_camiseta_ou_calca = probabilidade_camiseta + probabilidade_calca

print("A probabilidade de o cliente comprar uma camiseta ou uma calça é:", probabilidade_camiseta_ou_calca)


# Total de bilhetes numerados
total_bilhetes = 1000

# Total de bilhetes múltiplos de 5
total_multiplos_5 = total_bilhetes // 5

# Calculando a probabilidade de sortear um bilhete múltiplo de 5
probabilidade_multiplo_5 = total_multiplos_5 / total_bilhetes

print("A probabilidade de sortear um bilhete múltiplo de 5 é:", probabilidade_multiplo_5)

