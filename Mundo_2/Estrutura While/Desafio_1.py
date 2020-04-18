sex = str(input('Sexo [M / F]: ')).upper().strip()[0]
while sex not in 'MF':
        print('\033[1;31mDado incorreto, tente novamente por favor!!!\033[m')
        sex = str(input('Sexo [M / F]: ')).upper()
print('\n'
      '\033[32mDado do sexo {} registrado com sucesso!'.format(sex))