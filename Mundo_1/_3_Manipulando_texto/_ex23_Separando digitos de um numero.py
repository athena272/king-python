num_unico= int(input('Digite um número entre 0 à 9999, por favor: '))
uidade= num_unico // 1 % 10
dezena= num_unico // 10 % 10
centena= num_unico // 100 % 10
milhar= num_unico // 1000 % 10
print('''------------------------
O número foi {}
A unidade: {}
A dezena: {}
A centena: {}
A milha: {}'''.format(num_unico,uidade,dezena,centena,milhar))


