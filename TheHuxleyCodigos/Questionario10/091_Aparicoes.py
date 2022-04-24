listaNumeros = input().split()

numeroGetIndex = listaNumeros[-1]
posAparicoes = [numero for numero in listaNumeros if (numero == numeroGetIndex )]

print('O numero {} apareceu {} vezes'.format(numeroGetIndex, len(posAparicoes)))

