def velkmh(velocidadeInicial, aceleracao, tempo):
    velocidadeFinal = velocidadeInicial + (aceleracao * tempo) 

    return velocidadeFinal

# Carro 1
velocidadeCarro1 = float(input()) 
aceleraocaoCarro1 = float(input())
tempoCarro1 = float(input())
# Carro 2
velocidadeCarro2 = float(input()) 
aceleracaoCarro2 = float(input())
tempoCarro2 = float(input())
# Carro3
velocidadeCarro3 = float(input()) 
aceleracaoCarro3 = float(input())
tempoCarro3 = float(input())

carro1Final = velkmh(velocidadeCarro1, aceleraocaoCarro1, tempoCarro1) * 3.6 #converter em m/s

carro2Final = velkmh(velocidadeCarro2, aceleracaoCarro2, tempoCarro2) * 3.6 #converter em m/s

carro3Final = velkmh(velocidadeCarro3, aceleracaoCarro3, tempoCarro3) * 3.6 #converter em m/s

menorVelocidade = min(carro1Final, carro2Final, carro3Final)

print('%.1f' %menorVelocidade)