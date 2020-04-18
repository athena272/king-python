tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catoreze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')
while True:
    while True:
        numero_digitado = int(input('Digite um número entre [0 à 20]: '))
        if (numero_digitado >=0 and numero_digitado <= 20):
            break
        print('Faça novamente. ', end='')
    print('\033[1;33m-=-=\033[m' * 10)
    print(f'Você digitou o número {tupla[numero_digitado]}')
    print('\033[1;33m-=-=\033[m' * 10)
    pergunta = str(input('Deseja continuar? [s / n]: ')).strip().lower()[0]
    while pergunta not in 'sn':
        pergunta = str(input('Deseja continuar? [s / n]: ')).strip().lower()[0]
    if pergunta == 'n':
        break
print('=== OBRIGADO POR USAR MEU CÓDIGO ===')