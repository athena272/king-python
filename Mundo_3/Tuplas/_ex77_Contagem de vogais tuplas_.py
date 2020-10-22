words = ('aprender', 'programar', 'anjinho', 'python', 'java', 'guigo', 'paralelepipido', 'cubo', 'athena')
for palavra_unica in words:
    print(f'\nA palavra {palavra_unica.lower()} tem as vogais ', end='')
    for vogal in palavra_unica.lower():
        if vogal in 'aeiou':
            print(f' {vogal} ', end='')

