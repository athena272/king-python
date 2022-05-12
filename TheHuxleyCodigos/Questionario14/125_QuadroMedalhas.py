paises = {}

def somaLista(l1,l2):
    r = [l1[i] + l2[i] for i in range(len(l1))]
    return r

while True:
    try:
        paisMedalha = input().split(',')
        pais = paisMedalha[0]
        medalha = paisMedalha[1]
        if medalha == 'ouro':
            paises[pais] = somaLista(paises.get(pais,[0,0,0]),[1,0,0])
        elif medalha == 'prata':
            paises[pais] = somaLista(paises.get(pais,[0,0,0]),[0,1,0])
        else:
            paises[pais] = somaLista(paises.get(pais,[0,0,0]),[0,0,1])
    except:
        break

contador = 0
for medalhasPais in sorted(paises, key = paises.get, reverse=True):
    contador+=1
    pais = medalhasPais
    ouro = paises[medalhasPais][0]
    prata = paises[medalhasPais][1]
    bronze = paises[medalhasPais][2]
    print(f'{contador}){pais} ouro:{ouro} prata:{prata} bronze:{bronze}')