def qtdConsoante(sobrenome):
    letraAnterior = sobrenome[0]
    qtdSeguidas = 0
    for letra in sobrenome:
        if(qtdSeguidas >= 3):
            break
        if(letra not in 'aeiou' and letraAnterior not in 'aeiou'):
            qtdSeguidas += 1
        #Nao coloquei esse else na prova, mas eh necessario para resetar a contagem 
        else:
            qtdSeguidas = 1
        #A atualizacao da letraAnterior fica fora da condicao
        letraAnterior = letra
    
    return qtdSeguidas

sobrenome = input()
sobrenomeTestar = sobrenome.lower()

#Eu coloquei 4, mas devia ser maior ou igual 3
if(qtdConsoante(sobrenomeTestar) >= 3 and sobrenomeTestar[0] not in 'aeiou'):
    print(sobrenome, 'nao eh facil')

elif(qtdConsoante(sobrenomeTestar) >= 3 and sobrenomeTestar[0] in 'aeiou'):
    print(sobrenome, 'nao eh facil')

else:
    print(sobrenome, 'eh facil')

    