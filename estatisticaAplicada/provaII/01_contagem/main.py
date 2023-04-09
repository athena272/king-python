import math

# Número de funcionários
n_funcionarios = 5

# Número de cargos na comissão
n_cargos = 5

# Cálculo do número de maneiras de formar a comissão
num_maneiras = math.comb(n_funcionarios, 1) * math.comb(n_funcionarios-1, 1) * math.comb(n_funcionarios-2, 3)

print("O número de maneiras diferentes de formar a comissão é:", num_maneiras)


import math

# Número de camisetas de cada cor
n_azuis = 2
n_vermelhas = 3
n_amarelas = 5

# Número de camisetas no conjunto
n_conjunto = 3

# Cálculo do número de conjuntos possíveis
num_conjuntos = math.comb(n_azuis, 1) * math.comb(n_vermelhas, 1) * math.comb(n_amarelas, 1) + math.comb(n_azuis, 2) * math.comb(n_vermelhas, 1) + math.comb(n_azuis, 1) * math.comb(n_vermelhas, 2) + math.comb(n_azuis, 1) * math.comb(n_amarelas, 2)

print("O número de conjuntos possíveis é:", num_conjuntos)


import math

# Número de vagas para candidatos do sexo masculino
n_vagas_masc = 5

# Número de vagas para candidatos do sexo feminino
n_vagas_fem = 5

# Número de candidatos do sexo masculino
n_candidatos_masc = 8

# Número de candidatas do sexo feminino
n_candidatas_fem = 6

# Cálculo do número de maneiras de preencher as vagas
num_maneiras = math.comb(n_candidatos_masc, n_vagas_masc) * math.comb(n_candidatas_fem, n_vagas_fem)

print("O número de maneiras diferentes de preencher as vagas é:", num_maneiras)

import math

# Número de jogadores altos
n_jogadores_altos = 5

# Número de jogadores baixos
n_jogadores_baixos = 7

# Número de jogadores no quinteto titular
n_quinteto = 5

# Cálculo do número de maneiras de formar o quinteto titular
num_maneiras = math.comb(n_jogadores_altos, 3) * math.comb(n_jogadores_baixos, 2)

print("O número de maneiras diferentes de formar o quinteto titular é:", num_maneiras)

import math

# Número de livros de Matemática
n_livros_mat = 6

# Número de livros de Física
n_livros_fis = 5

# Número de livros de Química
n_livros_quim = 4

# Número de livros na prateleira
n_prateleira = 4

# Cálculo do número de maneiras de montar a prateleira
num_maneiras = math.comb(n_livros_mat, 1) * math.comb(n_livros_fis, 1) * math.comb(n_livros_quim, 1) * math.comb(n_livros_mat + n_livros_fis + n_livros_quim - 3, n_prateleira - 3)

print("O número de maneiras diferentes de montar a prateleira é:", num_maneiras)

