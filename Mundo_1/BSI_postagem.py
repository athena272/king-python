n = int(input('Digite o número de linhas: '))
j = n
for i in range(n+1):
    print(''*j + "*"*i)
    j-= 1