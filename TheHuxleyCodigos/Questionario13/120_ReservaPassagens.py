compahiaAerea={}
passageiros={}
codigos=[]
for aviao in range(37):
    valores=input().split()
    codigo=int(valores[0])
    vagas=int(valores[1])
    compahiaAerea[codigo]=compahiaAerea.get(codigo,0)+vagas 
    codigos.append(codigo)

while True:
    newvalores=input().split()
    cpf=int(newvalores[0])
    if cpf==9999:
        break 
    aviaodesejado=int(newvalores[1])
    passageiros[cpf]=passageiros.get(cpf,0)+aviaodesejado
for pessoa in passageiros:
    if passageiros[pessoa] not in codigos:
         print('INDISPONIVEL')
    else:
        if compahiaAerea[passageiros[pessoa]]==0:
            print('INDISPONIVEL')
        else:
            print(pessoa)
            compahiaAerea[passageiros[pessoa]]=compahiaAerea.get(passageiros[pessoa],compahiaAerea[passageiros[pessoa]])-1