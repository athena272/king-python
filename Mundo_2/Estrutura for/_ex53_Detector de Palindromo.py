#palíndrome, frase igual, mesmo ao contrário
frase = input('Digite uma frase: ').strip().lower()
words = frase.split()
juntar= ''.join(words)
inverso = ''
#inverso = juntar[::-1] outro modo de fazer
for letra in range(len(juntar) - 1, -1, -1):
    inverso += juntar[letra]
if (juntar == inverso):
    print('\033[4;33m{}\033[m ao inverso fica \033[4;36m{}\033[m'
          '\nentão a palavra \033[1;34mÉ\033[m um palíndromo'.format(juntar, inverso))
else:
    print('\033[4;33m{}\033[m ao inverso fica \033[4;36m{}\033[m'
          '\nentão a palavra \033[1;31mNÃO É\033[m um palíndromo'.format(juntar, inverso))