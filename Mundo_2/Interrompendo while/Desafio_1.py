soma = 0
contador = 0
while True:
    num = int(input('Digite um número [999 faz parar]: '))
    if (num == 999):
        break
    soma += num
    contador += 1
print(f'A soma de todos os \033[4;34m{contador}\033[m números, é {soma}')#Print mais moderno