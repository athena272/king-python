import pandas as pd

# Carregar os dados do arquivo CSV
dados = pd.read_csv("dados.csv")

# Visualizar as primeiras linhas do dataframe
print(dados.head())

# Contar o número de estudantes que praticam esportes
n_praticam_esportes = dados[dados['Esportes'] == 'Sim'].shape[0]
print("Número de estudantes que praticam esportes:", n_praticam_esportes)

# Contar o número de estudantes que estudam música
n_estudam_musica = dados[dados['Musica'] == 'Sim'].shape[0]
print("Número de estudantes que estudam música:", n_estudam_musica)

# Contar o número de estudantes que praticam esportes e estudam música
n_praticam_esportes_e_musica = dados[(dados['Esportes'] == 'Sim') & (dados['Musica'] == 'Sim')].shape[0]
print("Número de estudantes que praticam esportes e estudam música:", n_praticam_esportes_e_musica)

# Contar o número de estudantes que não praticam esportes nem estudam música
n_nao_praticam_esportes_nem_musica = dados[(dados['Esportes'] == 'Não') & (dados['Música'] == 'Não')].shape[0]
print("Número de estudantes que não praticam esportes nem estudam música:", n_nao_praticam_esportes_nem_musica)

# Calcular a porcentagem de estudantes que praticam esportes
porcentagem_praticam_esportes = (n_praticam_esportes / dados.shape[0]) * 100
print("Porcentagem de estudantes que praticam esportes: {:.2f}%".format(porcentagem_praticam_esportes))

# Calcular a probabilidade de estudar música dado que pratica esportes
probabilidade_musica_dado_esportes = n_praticam_esportes_e_musica / n_praticam_esportes
print("Probabilidade de estudar música dado que pratica esportes: {:.2f}%".format(probabilidade_musica_dado_esportes * 100))
