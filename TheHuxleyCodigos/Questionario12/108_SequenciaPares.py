def sequenciaPares(num):
    if num == 0:
        return print(0)
    else:
        if num % 2 == 0:
            return print(num), sequenciaPares(num-2)
        else:
            return sequenciaPares(num-1)

num = int(input())
(sequenciaPares(num))

