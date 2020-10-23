expression = list(input('Digite uma expressão matemática: '))
quantidade_esquerda = 0 #parenteses do lado esquerdo'('
quantidade_direita = 0 #parenteses do lado direito ')'
for i in expression:
    if (i == '('):
        quantidade_esquerda += 1
    elif (i == ')'):
        quantidade_direita += 1
if (quantidade_direita == quantidade_esquerda):
    print('expressão matemática VÁLIDA')
else:
    print('expressão matemática INVÁLIDA')