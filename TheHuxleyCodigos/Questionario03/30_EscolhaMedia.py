#(A - aritmética, H - harmônica, G - geométrica)
tipoMedia = input()

num1 = int(input())
num2 = int(input())
num3 = int(input())

media = (num1 + num2 + num3) / 3

if(tipoMedia == 'H'):
    media = (3 / ((1/num1) + (1/num2) + (1/num3)))

if(tipoMedia == 'G'):
    media = (num1 * num2 * num3) ** (1/3)

print('%.3f' %media)

