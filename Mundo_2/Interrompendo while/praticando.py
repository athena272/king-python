soma = 0
while True:
    num = int(input('Digite um número [999 faz parar]: '))
    if num == 999:
        break
    soma += num
print(f'A soma dos números é {soma}')#Print mais moderno