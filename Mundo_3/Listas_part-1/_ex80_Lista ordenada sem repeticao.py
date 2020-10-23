order_lista = [] #lista vazia
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    #começo da lista
    if (i == 0) or (num > order_lista[-1]): #-1 mesmo que último elemento
        order_lista.append(num)
        print('Adicionado ao fim da lista')
    else:
        pos = 0
        while (pos < len(order_lista)):
            if (num <= order_lista[pos]):
                order_lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {order_lista}')