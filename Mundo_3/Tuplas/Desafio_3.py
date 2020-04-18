from random import randint
computador = (randint(0 , 50), randint(0 , 50), randint(0 , 50), randint(0 , 50), randint(0 , 50))
print('Os valores foram: ', end='')
for i in computador:
    print(f' {i} ', end='')
print(f'\n O maior valor sorteado foi: {max(computador)}'
      f'\n O menor valor sorteado foi: {min(computador)}')
