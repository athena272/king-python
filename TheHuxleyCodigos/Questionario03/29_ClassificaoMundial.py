pontosPartida1 = int(input())
pontosPartida2 = int(input())
pontosPartida3 = int(input())
pontosPartida4 = int(input())
pontosPartida5 = int(input())
pontosPartida6 = int(input())

somatorio = pontosPartida1 + pontosPartida2 + pontosPartida3 + pontosPartida4 + pontosPartida5 + pontosPartida6

estaClassificado = 'Classificado'

if(somatorio < 100):
    estaClassificado = 'Eliminado'

print(estaClassificado)
