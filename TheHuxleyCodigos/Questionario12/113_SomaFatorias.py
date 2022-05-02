def calcFatorial(num):
    if num == 0:
        return 1 

    fatorial = num * calcFatorial(num - 1)
    return fatorial

def serMult3(num):
    status = False
    if(num % 3 == 0):
        status = True
    return status

soma = 0
for i in range(0, 5):
    num = int(input())
    if serMult3(num):
        soma += calcFatorial(num)

print(soma)