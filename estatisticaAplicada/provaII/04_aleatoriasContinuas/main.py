# um submódulo do pacote "scipy" que fornece uma ampla variedade de funções e classes para trabalhar com estatísticas e distribuições de probabilidade. Ele inclui implementações de várias distribuições de probabilidade, como normal, exponencial, uniforme, binomial, entre outras, juntamente com funções para cálculos estatísticos, geração de números aleatórios, ajuste de distribuições, entre outros recursos estatísticos.
import scipy.stats as stats

# Taxa de chegada de clientes por minuto
taxa_chegada = 0.1

# Tempo máximo de espera em minutos
tempo_max_espera = 5

# Criando a distribuição exponencial
distribuicao_exponencial = stats.expon(scale=1/taxa_chegada)

# Calculando a probabilidade de esperar menos de 5 minutos na fila
probabilidade_espera_menos_5min = distribuicao_exponencial.cdf(tempo_max_espera)

print("A probabilidade de esperar menos de 5 minutos na fila é:", probabilidade_espera_menos_5min)


import scipy.stats as stats
# Média do tempo de vida das lâmpadas em horas
media_vida_lampadas = 2000

# Desvio padrão do tempo de vida das lâmpadas em horas
desvio_padrao_vida_lampadas = 100

# Tempo mínimo de duração da lâmpada em horas
tempo_min_duracao = 2200

# Criando a distribuição normal
distribuicao_normal = stats.norm(loc=media_vida_lampadas, scale=desvio_padrao_vida_lampadas)

# Calculando a probabilidade de uma lâmpada durar mais de 2200 horas
probabilidade_duracao_mais_2200h = 1 - distribuicao_normal.cdf(tempo_min_duracao)

print("A probabilidade de uma lâmpada durar mais de 2200 horas é:", probabilidade_duracao_mais_2200h)

import scipy.stats as stats

# Parâmetros da distribuição normal
media = 170
desvio_padrao = 5

# a) Probabilidade de altura entre 165 cm e 175 cm
probabilidade_a = stats.norm.cdf(175, loc=media, scale=desvio_padrao) - stats.norm.cdf(165, loc=media, scale=desvio_padrao)

# b) Probabilidade de altura maior que 180 cm
probabilidade_b = 1 - stats.norm.cdf(180, loc=media, scale=desvio_padrao)

# c) Altura abaixo dos 25% mais baixos
altura_25_percentil = stats.norm.ppf(0.25, loc=media, scale=desvio_padrao)

# Resultados
print("a) Probabilidade de altura entre 165 cm e 175 cm: {:.4f}".format(probabilidade_a))
print("b) Probabilidade de altura maior que 180 cm: {:.4f}".format(probabilidade_b))
print("c) Altura abaixo dos 25% mais baixos: {:.2f} cm".format(altura_25_percentil))

import scipy.stats as stats

# Parâmetros da distribuição exponencial
taxa_chegada = 0.2

# a) Probabilidade de esperar menos de 5 minutos
probabilidade_a = stats.expon.cdf(5, scale=1/taxa_chegada)

# b) Tempo de espera mediano
tempo_mediano = stats.expon.ppf(0.5, scale=1/taxa_chegada)

# Resultados
print("a) Probabilidade de esperar menos de 5 minutos: {:.4f}".format(probabilidade_a))
print("b) Tempo de espera mediano: {:.2f} minutos".format(tempo_mediano))


import scipy.stats as stats

# Parâmetros da distribuição Weibull
k = 2
lambda_ = 100

# a) Probabilidade de vida inferior a 200 horas
probabilidade_a = stats.weibull_min.cdf(200, c=k, scale=lambda_)

# b) Tempo de vida médio
tempo_vida_medio = stats.weibull_min.mean(c=k, scale=lambda_)

# Resultados
print("a) Probabilidade de vida inferior a 200 horas: {:.4f}".format(probabilidade_a))
print("b) Tempo de vida médio: {:.2f} horas".format(tempo_vida_medio))

