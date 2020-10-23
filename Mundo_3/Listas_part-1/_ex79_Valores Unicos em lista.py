LISTA = list()
while True:
    num = int(input("Digite um valor, por favor: ")) #receber valores do usário
    # Tirar valores repetidos
    if (num not in LISTA):
        LISTA.append(num)
        print('Valor adicionador com sucesso')
    else:
        print("Valor duplicado, não será adicionado...")
    #Continuar ou não a repetição
    continuar = str(input("Desja continuar?[S/N]: ")).strip().lower()[0]
    if (continuar == 'n'):
        break
print(f'A lista foi {LISTA}')
