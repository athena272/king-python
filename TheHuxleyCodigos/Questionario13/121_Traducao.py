while True:
    regras={}
    novastrings=[]
    numeros=input().split()
    numRegras=int(numeros[0])
    numLinhas=int(numeros[1])
    if numRegras==0 and numLinhas==0:
        break
    for valor in range(numRegras):
        mudanca=input().split()
        regras[mudanca[0]]=regras.get(mudanca[0],'')+mudanca[2]
    for valor in range(numLinhas):
        texto=input()
        for regra in regras:
            if regra not in texto:
                texto=texto
            else:
                texto=texto.replace(regra,regras[regra])
        novastrings.append(texto)
    for frase in novastrings:
        print(frase)
    regras.clear()
    novastrings.clear()