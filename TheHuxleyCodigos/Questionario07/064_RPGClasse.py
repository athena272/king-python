def ehKnight(forca, destreza, peso):
    serKnight = False
    if(forca > 5 and destreza > 5 and peso > 5):
        serKnight = True
    
    return serKnight


def ehMage(forca, inteligencia, furtividade, peso):
    serMage = False
    if(forca < 5 and inteligencia > 5 and furtividade > 5 and peso < 5):
        serMage = True
    
    return serMage


def ehPaladin(forca, inteligencia, destreza, furtividade, peso):
    serPaladin = False
    if(forca > 5 and inteligencia > 5 and destreza > 5 and furtividade > 5 and peso < 5):
        serPaladin = True
    
    return serPaladin


def ehOrc(forca, inteligencia, destreza, furtividade, peso):
    serOrc = False
    if(forca > 10 and inteligencia < 5 and destreza < 5 and furtividade < 5 and peso > 5):
        serOrc = True
    
    return serOrc


forca = int(input())
inteligencia = int(input())
destreza = int(input())
furtividade = int(input())
peso = int(input())

classe = ''
if(ehKnight(forca, destreza, peso)):
    classe = 'Knight'
elif(ehMage(forca, inteligencia, furtividade, peso)):
    classe = 'Mage'
elif(ehPaladin(forca, inteligencia, destreza, furtividade, peso)):
    classe = 'Paladin'
elif(ehOrc(forca, inteligencia, destreza, furtividade, peso)):
    classe = 'Orc'

print(classe)
    