name=input('Digite seu nome, por favor: ').strip().title()
name_dividio= name.split()
print(''' --------------
Muito prazer em te conhecer "{}"!
seu primeiro nome é: {}
seu último nome é: {}'''.format(name,name_dividio[0], name_dividio[len(name_dividio)-1]))
print(name_dividio)
