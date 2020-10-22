name= input('Por favor, digite seu nome: ').strip()
name_dividio= name.split()
if (name_dividio[0].upper() == 'SANTO'):
    print('''A sua cidade começa com Santo
    -----------------------------f
    {}'''.format(name))
