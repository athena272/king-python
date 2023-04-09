import pandas as pd
import numpy as np

# Definir o número de linhas do CSV
n_linhas = 50

# Gerar valores aleatórios para as colunas "Esportes" e "Música"
esportes = np.random.choice(['Sim', 'Nao'], size=n_linhas)
musica = np.random.choice(['Sim', 'Nao'], size=n_linhas)

# Criar DataFrame com os dados gerados
dados = pd.DataFrame({'Esportes': esportes, 'Musica': musica})

# Salvar os dados em um arquivo CSV
dados.to_csv('dados.csv', index=False)

print("Arquivo CSV gerado com sucesso!")
