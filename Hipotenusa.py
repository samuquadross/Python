import math
o = float(input('Digite o Cateto Oposto: '))
a = float(input('Digite o Cateto Adjacente: '))
h = math.hypot(o,a)
print('='*37)
print('A hipotenusa do trinângulo é: {:.2f}'.format(h))
print('='*37)