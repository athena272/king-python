print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
      '\n  Verificar se é maior de Idade'
      '\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

jovemIdade = int(input('Olá jovem, qual a sua idade?: ')) #recebe a idade da pessoa e guarda esse valor

if jovemIdade < 18:
    
    print(f'Você ainda é menor de idade, você tem apenas {jovemIdade} anos!!!')

else:
    print(f'Você já é maior de idade, você tem {jovemIdade} anos!!!')

    