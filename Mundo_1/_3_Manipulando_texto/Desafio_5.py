#encontrando o 'A'
frase= input('Digite aqui uma frase, por favor: ').strip()
print('''---------------''')
print('A letra "a" aparece {} vezes na frase'.format(frase.lower().count('a')))
print('O primeiro "a" está na [{}ª] posição'.format(frase.lower().find('a')+1))
print('O último "a" está na [{}ª] posição'.format(frase.lower().rfind('a')+1))