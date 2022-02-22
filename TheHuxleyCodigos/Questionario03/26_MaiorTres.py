num1 = int(input())
num2 = int(input())
num3 = int(input())

menor = num3

if(num1 <= num2 and num1 <= num3):
    menor = num1
if(num2 <= num1 and num2 <= num3):
    menor = num2

#funcao min: menor = min(num1, num2, num3)

print(menor)