ph = float(input())

if(ph < 0 or ph > 14):
    print("Digite o pH da solucao:")
    print('Valor deve estar entre 0 e 14.')
elif(ph < 7):
    solucao = 'acida'
    print("Digite o pH da solucao:")
    print(f'Essa solucao e {solucao}.')
elif(ph > 7):
    solucao = 'basica'
    print("Digite o pH da solucao:")
    print(f'Essa solucao e {solucao}.')
elif(ph == 7):
    solucao = 'neutra'
    print("Digite o pH da solucao:")
    print(f'Essa solucao e {solucao}.')
