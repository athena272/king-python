algarismo = int(input())

if(algarismo > 0):
    algarismoUnidade = (algarismo % 10)
else:
    algarismoUnidade = ((algarismo * -1) % 10) #primeiro deixa ele o algorismo positivo, para não adulterar o resto da divisao
    algarismoUnidade = (algarismoUnidade * -1) #Por fim, deixa negativo
   
print(algarismoUnidade)







