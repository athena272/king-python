print('=== Tinta para pintar parede ===')
largura= float(input('Qual a largura da parede em metros?: '))
altura= float(input('Qual a altura da parede em metros?: '))
area= altura*largura
tinta= area/2
print('A medida da sua parede é de \033[4;34m{} x {}(m)\033[m e \033[4;32mtem {:.2f}(m²)\033[m'.format(largura, altura, area))
print('\033[4;35m---UM LITRO DE TINTA PINTA 2 METROS QUADRADOS----\033[m')
print('Serão necessários \033[1;31m{:.2f}\033[m litros de tinta para pintar a parede de \033[1;33m{:.2f}(m²)'.format(tinta, area))
