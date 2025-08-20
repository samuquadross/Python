import random
from random import randint

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
p = (n1,n2,n3,n4)
sorteio = random.choice(p)
print('='*22)
print('O sorteado foi: {}'.format(sorteio))
print('='*22)
