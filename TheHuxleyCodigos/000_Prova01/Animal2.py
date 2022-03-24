def nomeAnimal(tipoColuna, familia, come):
    animal = 'sanguessuga'
    if(tipoColuna == 'vertebrado' and familia == 'ave' and come == 'carnivoro'):
        animal = 'aguia'
    elif(tipoColuna == 'vertebrado' and familia == 'ave' and come == 'onivoro'):
        animal = 'pomba'
    elif(tipoColuna == 'vertebrado' and familia == 'mamifero' and come == 'onivoro'):
        animal = 'homem'
    elif(tipoColuna == 'vertebrado' and familia == 'mamifero' and come == 'herbivoro'):
        animal = 'vaca'
    elif(tipoColuna == 'invertebrado' and familia == 'inseto' and come == 'hematofago'):
        animal = 'pulga'
    elif(tipoColuna == 'invertebrado' and familia == 'inseto' and come == 'herbivoro'):
        animal = 'lagarta'
    elif(tipoColuna == 'invertebrado' and familia == 'anelideo' and come == 'onivoro'):
        animal = 'minhoca'

    return animal

while True:
    informacao = input().lower()
    if(informacao == '*'):
        break
    
    informacao = informacao.split()
    coluna = informacao[0]
    familia = informacao[1]
    comida = informacao[2]
    
    tipoAnimal = nomeAnimal(coluna, familia, comida)

    print(tipoAnimal)

