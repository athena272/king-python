ano = int(input())

ehBissexto = 'NAOBISSEXTO'

if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
    ehBissexto = 'BISSEXTO'

print(ehBissexto)
