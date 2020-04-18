from math import sin, cos, tan, radians
angule= float(input('Digite um valor de ângulo: '))
seno= sin(radians(angule))
coseeno= cos(radians(angule))
tangente= tan(radians(angule))
print('O ângulo {} possui: '
      '\nSENO: {:.2f}'
      '\nCOSSENO: {:.2f} '
      '\nTANGENTE: {:.2f} '.format(angule, seno, coseeno, tangente))