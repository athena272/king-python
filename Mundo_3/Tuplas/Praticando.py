#tupla ()
#lista []
#dicionário {}
lanche = ('Lasanha', 'Batata Frite', 'Fanta', 'Sorvete')
#tuplas são imutáveis
#lanche[3] = 'Refrigerante'
#print(lanche)
for i in range(0, len(lanche)):
    print(lanche[i])
for i in lanche:
    print(i)
for pos, i in enumerate(lanche):
    print(f'A comida {i} na posição {pos}')
print(lanche.index('Lasanha'))