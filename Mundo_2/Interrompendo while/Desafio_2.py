while True:
    num = int(input('De que número deseja saber a tabuada? [negativos encerram]: '))
    if (num < 0):
        break
    for i in range(1, 11):
        multi = i * num
        print(f'{i} X {num} = {multi}')
    print('\033[1;36m-\033[m' * 30, end='')
    print('')
print('\033[32mTHE END do programa da tabuada, obrigado!!!')