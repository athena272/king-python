def fat(num):
    if num == 0:
        return 1 

    fatorial = num * fat(num - 1)
    return fatorial


while True:
    num = int(input())
    if num == -1:
        break
    print(fat(num))