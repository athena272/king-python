from random import randint
from time import sleep
computador_escolhido= randint(0,5)
print('Eu pensei no número entre 0 à 5...')
palpite= int(input('Tente advinha qual foi: '))
print('processando...')
sleep(4)
if computador_escolhido == palpite:
    print('Parabéns você acertou, o número sorteado realmente foi {}'.format(computador_escolhido))
else:
    print('É uma pena, mas você errou, o número não foi {}, mas sim {}'.format(palpite,computador_escolhido))